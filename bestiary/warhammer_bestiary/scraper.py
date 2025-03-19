"""Scrap StatBlocks from https://wfrp1e.fandom.com/wiki/Category:Bestiary and save to file."""

import json
import logging
from functools import cached_property
from pathlib import Path
from typing import ClassVar, Final

import requests
from bs4 import BeautifulSoup

URI_ROOT = "https://wfrp1e.fandom.com"

BEASTIARY_STARTING_PAGE = "/wiki/Category:Bestiary"

OUTPUT_FILE = Path("beasts.json")
LOG_FILE = Path("beasts.log")

log = logging.getLogger(__name__)
logfile = logging.FileHandler(LOG_FILE)
logfile.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
logfile.setFormatter(formatter)
log.addHandler(logfile)
log.setLevel(logging.INFO)


def get_and_parse(uri: str, session: requests.Session) -> BeautifulSoup:  # noqa: D103
    _raw = session.get(uri, timeout=10)
    log.debug("Parsing %s", uri)
    return BeautifulSoup(_raw.text, features="html.parser")


class WikiPage:
    """
    A https://wfrp1e.fandom.com page that contains statblocks.
    
    Subclass this for each page category and provide concrete implementations of:
    - `is_statblock` - how to identify a statblock in the page soup
    - `parse_statblock` - how to find the title and stats from the soup of a statblock

    All other methods & properties should work out of the box.
    """

    STARTING_PAGE: ClassVar[str]
    """URI of the contents page for this type of information."""

    def is_statblock(self, soup: BeautifulSoup) -> bool:
        """
        How to recognise a statblock. Returns `True` if a tag represents a statblock.

        Varies based on page design, must be defined in each Subclass.
        """
        msg = f"{type(self)} has not defined `statblocks`."
        raise NotImplementedError(msg)
    
    @classmethod
    def parse_statblock(cls, blocksoup: BeautifulSoup) -> tuple[str, dict[str, str | int]]:
        """
        Parse a block of soup and return the statblock title and a dict of the parsed stats.
        
        The form of `soupblock` varies based on page design, so this must be defined in each Subclass.
        """
        msg = f"{cls.__name__} has not defined `parse_statblock`."
        raise NotImplementedError(msg)

    def __init__(self, uri: str, session: requests.Session | None) -> None:
        """Initialise WikiPage for a given `uri`."""
        self.uri = uri
        self.session = session or requests.Session()

    @cached_property
    def soup(self) -> BeautifulSoup:
        """A BeautifulSoup of the page."""
        return get_and_parse(self.uri, self.session)

    @property
    def title(self) -> str:
        """The simple page title without the site details."""
        return self.soup.title.getText().split("|")[0].strip()

    @property
    def statblocksoup(self) -> list[BeautifulSoup]:
        """The Soup for each stat block."""
        return self.soup.find_all(self.is_statblock)

    @classmethod
    def parse_stat(cls, val: str) -> int | str:
        """Handle cases where values may be missing or given as dice rolls etc."""
        if not val or val == "-":
            return 0
        try:
            return int(val)
        except ValueError:
            # E.g. "d6" or "3-5"
            return val

    @property
    def statblocks(self) -> dict[str, dict[str, int | str]]:
        """All the page's statblocks, parsed by the class-specific `parse_statblock` method."""
        return dict(self.parse_statblock(blocksoup) for blocksoup in self.statblocksoup)


class Beast(WikiPage):
    """A page for a normal member of the bestiary, with the stat block shown vertically at the side of the page."""

    def is_statblock(self, soup: BeautifulSoup) -> bool:
        """Statblocks are in an `aside` tag with class `type-stat`."""
        return "type-stat" in soup.get("class", "")

    @classmethod
    def parse_statblock(cls, blocksoup: BeautifulSoup) -> tuple[str, dict[str, str | int]]:
        """Stat value is tagged with class `pi-data`and `data-source` attribute showing the stat name."""
        title = blocksoup.find(class_="pi-header").getText()
        stats = {
            stat["data-source"]: cls.parse_stat(stat.find(class_="pi-data-value").getText())
            for stat in blocksoup.find_all(class_="pi-data")
        }
        return title, stats


class NPC(WikiPage):
    """NPCs have stat blocks in a horizontal table in the text."""

    STARTING_PAGE: Final = "/wiki/Category:NPCs"

    def is_statblock(self, soup: BeautifulSoup) -> bool:
        """Stat Blocks are in tables of class `article-table`."""
        return soup.name == "table" and "article-table" in soup.get("class", "")

    @classmethod
    def parse_statblock(cls, blocksoup: BeautifulSoup) -> tuple[str, dict[str, str | int]]:
        """No tags and no title. Need to parse a table & provide `''` as title."""
        title = ""
        tablerows = blocksoup.find_all("tr")
        # TODO: add some kind of check that we only have two rows ...
        statnames = [cell.get_text(strip=True) for cell in tablerows[0].find_all("th")]
        statvalues = [cls.parse_stat(cell.get_text(strip=True)) for cell in tablerows[1].find_all("td")]
        stats = dict(zip(statnames, statvalues, strict=True))
        return title, stats


if __name__ == "__main__":
    log.info("Parsing Beastiary")

    beastiary = get_and_parse(BEASTIARY_STARTING_PAGE)

    log.debug("Got Beastiary Index")

    beast_pages = beastiary.find_all("a", class_="category-page__member-link")

    log.info("Found %i beasts.", len(beast_pages))
    log.debug("Beast content pages: %r", beast_pages)

    beast_page_contents = {link.attrs["title"]: get_and_parse(link.attrs["href"]) for link in beast_pages}

    log.debug("Parsed all pages")

    beasts = {
        log.info("Getting %s", beast) or beast: Beast.get_stats(beast_page)
        for beast, beast_page in beast_page_contents.items()
    }

    log.info("Got %i beasts", len(beasts))
    log.debug("Got: %r", beasts)

    OUTPUT_FILE.write_text(json.dumps(beasts, indent=2))
    log.info("Written data to %s", OUTPUT_FILE)
