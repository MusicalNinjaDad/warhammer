"""Scrap StatBlocks from https://wfrp1e.fandom.com/wiki/Category:Bestiary and save to file."""

import json
import logging
import urllib.parse
from functools import cached_property
from pathlib import Path
from typing import ClassVar, Final

import requests
from bs4 import BeautifulSoup

LOG_FILE = Path("beast_scraper.log")

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
    - `CATEGORY_INDEX` - the category index uri
    - `is_page_link` - a filter function to apply when parsing `CATEGORY_INDEX`

    All other methods & properties should work out of the box.
    """

    CATEGORY_INDEX: ClassVar[str]
    """URI of the contents page for this type of information."""

    @classmethod
    def is_page_link(cls, tag: BeautifulSoup) -> bool:
        """
        How to recognise a valid page link. Returns `True` if a tag links to a page of interest.

        Varies based on category, must be defined in each Subclass, but probably needs to include `name`=="a".
        """
        msg = f"{cls.__name__} has not defined `is_page_link`."
        raise NotImplementedError(msg)

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

    def __init__(self, uri: str, session: requests.Session | None = None) -> None:
        """Initialise WikiPage for a given `uri`."""
        log.info("Initialising %s for %s", type(self), uri)
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

    @property
    def statblocks(self) -> dict[str, dict[str, int | str]]:
        """All the page's statblocks, parsed by the class-specific `parse_statblock` method."""
        log.info("Getting statblocks for %s", self.title)
        return dict(self.parse_statblock(blocksoup) for blocksoup in self.statblocksoup)

    @classmethod
    def absolute(cls, uri: str) -> str:
        """Return dull URI for a partial address, using `CATEGORY_INDEX` as the root."""
        root = urllib.parse.urlsplit(cls.CATEGORY_INDEX)
        reluri = urllib.parse.urlsplit(uri)
        absuri = urllib.parse.SplitResult(
            scheme=root.scheme if reluri.scheme == "" else reluri.scheme,
            netloc=root.netloc if reluri.netloc == "" else reluri.netloc,
            path=reluri.path,
            query=reluri.query,
            fragment=reluri.fragment,
        )
        return absuri.geturl()

    @classmethod
    def get_page_uris(cls, session: requests.Session | None = None) -> dict[str, str]:
        """List the relevant uris from the `CATGEORY_INDEX`."""
        session = requests.Session() if session is None else session
        indexsoup = get_and_parse(cls.CATEGORY_INDEX, session)
        return {link.attrs["title"]: link.attrs["href"] for link in indexsoup.find_all(cls.is_page_link)}


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


class Beast(WikiPage):
    """A page for a normal member of the bestiary, with the stat block shown vertically at the side of the page."""

    CATEGORY_INDEX: Final = "https://wfrp1e.fandom.com/wiki/Category:Bestiary"

    @classmethod
    def is_page_link(cls, tag: BeautifulSoup) -> bool:
        """Beast_pages = beastiary.find_all("a", class_="category-page__member-link")."""
        return (
            tag.name == "a"
            and "category-page__member-link" in tag.get("class", "")
            and "(NPC)" not in tag.attrs["title"]
        )
    
        
    @classmethod
    def is_vertical_statblock(cls, soup: BeautifulSoup) -> bool:
        """Vertical statblocks are on basic Beast pages in an `aside` tag with class `type-stat`."""
        return "type-stat" in soup.get("class", "")
    
    @classmethod
    def is_horizontal_statblock(cls, soup: BeautifulSoup) -> bool:
        """Horizontal statblocks are on NPCs and beasts with multiple blocks, in tables of class `article-table`."""
        return soup.name == "table" and "article-table" in soup.get("class", "")

    @classmethod
    def is_statblock(cls, soup: BeautifulSoup) -> bool:
        """Statblocks are in an `aside` tag with class `type-stat`."""
        return cls.is_vertical_statblock(soup) or cls.is_horizontal_statblock(soup)

    @classmethod
    def parse_statblock(cls, blocksoup: BeautifulSoup) -> tuple[str, dict[str, str | int]]:
        """Stat value is tagged with class `pi-data`and `data-source` attribute showing the stat name."""
        title = blocksoup.find(class_="pi-header").getText()
        try:
            stats = {
                stat["data-source"]: cls.parse_stat(stat.find(class_="pi-data-value").getText())
                for stat in blocksoup.find_all(class_="pi-data")
            }
        except Exception:
            log.exception("Error parsing stats for %s - Blocksoup: %r", cls.__name__, blocksoup)
        return title, stats


class NPC(WikiPage):
    """NPCs have stat blocks in a horizontal table in the text."""

    CATEGORY_INDEX: Final = "https://wfrp1e.fandom.com/wiki/Category:NPCs"

    @classmethod
    def is_page_link(cls, tag: BeautifulSoup) -> bool:
        """No need to filter out any results."""
        return tag.name == "a" and "category-page__member-link" in tag.get("class", "")

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
        try:
            stats = dict(zip(statnames, statvalues, strict=True))
        except ValueError:
            log.exception("Error parsing stats for %s - Blocksoup: %r", cls.__name__, blocksoup)
        return title, stats


if __name__ == "__main__":
    
    log.info("Begin scraping Beasts")
    beast_pages = [Beast.absolute(uri) for uri in Beast.get_page_uris()]
    beasts = [Beast(page) for page in beast_pages]
    beastfile = Path("beasts.json")
    beastfile.write_text(json.dumps({beast.title: beast.statblocks for beast in beasts}, indent=2))
    log.info("%i beasts written to %s", len(beasts), beastfile)

    log.info("Begin scraping NPCs")
    npc_pages = [NPC.absolute(uri) for uri in NPC.get_page_uris()]
    npcs = [NPC(page) for page in npc_pages]
    npcfile = Path("npcs.json")
    npcfile.write_text(json.dumps({npc.title: npc.statblocks for npc in npcs}, indent=2))
    log.info("%i NPCs written to %s", len(npcs), npcfile)