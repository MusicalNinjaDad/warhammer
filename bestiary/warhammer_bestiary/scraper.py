"""Scrap StatBlocks from https://wfrp1e.fandom.com/wiki/Category:Bestiary and save to file."""

import json
import logging
import urllib.parse
from functools import cached_property
from pathlib import Path
from typing import ClassVar, Final

import requests
from bs4 import BeautifulSoup

BEASTFILE = Path("beasts.json")
NPCFILE = Path("npcs.json")

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


class BlockParser:
    """Identify, store and parse the soup for a StatBlock."""

    MAGIC_STAT_STRING: Final[str] = "MWSBSSTWIADexLdIntClWPFel"

    @classmethod
    def filter(cls, soup: BeautifulSoup) -> bool:
        """Filter to pass to `bs4.find_all` to identify this type of Block."""
        msg = f"{cls} has not defined `filter`."
        raise NotImplementedError(msg)

    def parse(self) -> tuple[tuple[str, str], dict[str, int | str]]:
        """Parse the block and return `((section_title, block_title), stats)`."""
        msg = f"{type(self)} has not defined `parse`."
        raise NotImplementedError(msg)

    def __init__(self, soup: BeautifulSoup) -> None:
        """Store the soup."""
        self.soup = soup

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


class UntitledBlock(BlockParser):
    """Horizontal statblocks are on NPCs and beasts with multiple blocks, some have no title."""

    @classmethod
    def filter(cls, soup: BeautifulSoup) -> bool:
        """In tables of class `article-table`."""
        return (
            soup.name == "table"
            and "article-table" in soup.get("class", "")
            and soup.find("tr").getText(strip=True) == cls.MAGIC_STAT_STRING
        )

    def parse(self) -> tuple[tuple[str, str], dict[str, int | str]]:
        """No tags and no title. Need to parse a table & provide `''` as title."""
        try:
            group = self.soup.find_previous_sibling("h3").find("span", class_="mw-headline").getText(strip=True)
        except AttributeError:
            group = ""
        title = "Basic Profile"
        tablerows = self.soup.find_all("tr")
        # TODO: add some kind of check that we only have two rows ...
        statnames = [cell.get_text(strip=True) for cell in tablerows[0].find_all("th")]
        statvalues = [self.parse_stat(cell.get_text(strip=True)) for cell in tablerows[1].find_all("td")]
        try:
            stats = dict(zip(statnames, statvalues, strict=True))
        except ValueError:
            log.exception("Error parsing stats for %s - Blocksoup: %r", type(self).__name__, self.soup)
        return (group, title), stats


class TitledBlock(BlockParser):
    """Horizontal statblocks are on NPCs and beasts with multiple blocks, some have a title."""

    @classmethod
    def filter(cls, soup: BeautifulSoup) -> bool:
        """In tables of class `article-table`."""
        return (
            soup.name == "table"
            and "article-table" in soup.get("class", "")
            and soup.find("tr").getText(strip=True) != cls.MAGIC_STAT_STRING
            and cls.MAGIC_STAT_STRING in [row.getText(strip=True) for row in soup.find_all("tr")]
        )

    def parse(self) -> tuple[tuple[str, str], dict[str, int | str]]:
        """No tags and no title. Need to parse a table & provide `''` as title."""
        try:
            group = self.soup.find_previous_sibling("h3").find("span", class_="mw-headline").getText(strip=True)
        except AttributeError:
            group = ""
        tablerows = self.soup.find_all("tr")
        title = tablerows[0].getText(strip=True)
        statnames = [cell.get_text(strip=True) for cell in tablerows[1].find_all("td")]
        statvalues = [self.parse_stat(cell.get_text(strip=True)) for cell in tablerows[2].find_all("td")]
        try:
            stats = dict(zip(statnames, statvalues, strict=True))
        except ValueError:
            log.exception("Error parsing stats for %s - Blocksoup: %r", type(self).__name__, self.soup)
        return (group, title), stats


class VerticalBlock(BlockParser):
    """Vertical statblocks are on basic Beast pages."""

    @classmethod
    def filter(cls, soup: BeautifulSoup) -> bool:
        """In an `aside` tag with class `type-stat`."""
        return "type-stat" in soup.get("class", "")

    def parse(self) -> tuple[str, dict[str, int | str]]:
        """Stat value is tagged with class `pi-data`and `data-source` attribute showing the stat name."""
        group = ""
        title = self.soup.find(class_="pi-header").getText()
        try:
            stats = {
                stat["data-source"]: self.parse_stat(stat.find(class_="pi-data-value").getText())
                for stat in self.soup.find_all(class_="pi-data")
            }
        except Exception:
            log.exception("Error parsing stats for %s - Blocksoup: %r", type(self).__name__, self.soup)
        return (group, title), stats


class WikiPage:
    """A https://wfrp1e.fandom.com page that contains statblocks."""

    CATEGORY_INDEX: ClassVar[str]
    """URI of the contents page for this type of information."""
    parsers: ClassVar[list[BlockParser]] = [VerticalBlock, UntitledBlock, TitledBlock]

    @classmethod
    def is_page_link(cls, tag: BeautifulSoup) -> bool:
        """
        How to recognise a valid page link. Returns `True` if a tag links to a page of interest.

        Varies based on category, must be defined in each Subclass, but probably needs to include `name`=="a".
        """
        msg = f"{cls.__name__} has not defined `is_page_link`."
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
        return self.soup.title.getText().split("|")[0].strip().removesuffix("(NPC)").strip()

    @property
    def statblocks(self) -> list[BlockParser]:
        """All the page's statblocks."""
        log.info("Getting statblocks for %s", self.title)
        return [parser(blocksoup) for parser in self.parsers for blocksoup in self.soup.find_all(parser.filter)]

    def as_dict(self) -> dict[str, dict[str, int | str]]:
        """The statblocks as a dict, indexed by statblock title."""
        statsdict = {}
        for statblock in self.statblocks:
            (group, title), stats = statblock.parse()
            try:
                statsdict[group][title] = stats
            except KeyError:
                statsdict[group] = {title: stats}
        return statsdict

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


class NPC(WikiPage):
    """NPCs have stat blocks in a horizontal table in the text."""

    CATEGORY_INDEX: Final = "https://wfrp1e.fandom.com/wiki/Category:NPCs"

    @classmethod
    def is_page_link(cls, tag: BeautifulSoup) -> bool:
        """No need to filter out any results."""
        return tag.name == "a" and "category-page__member-link" in tag.get("class", "")


if __name__ == "__main__":
    ignore = ["https://wfrp1e.fandom.com/Bestiary"]
    log.info("Begin scraping NPCs")
    npc_pages = [NPC.absolute(uri) for uri in NPC.get_page_uris()]
    npcs = [WikiPage(page) for page in npc_pages if page not in ignore]
    NPCFILE.write_text(json.dumps({npc.title: npc.as_dict() for npc in npcs}, indent=2))
    ignore += npc_pages
    log.info("%i NPCs written to %s", len(npcs), NPCFILE)

    log.info("Begin scraping Beasts")
    beast_pages = [Beast.absolute(uri) for uri in Beast.get_page_uris()]
    beasts = [WikiPage(page) for page in beast_pages if page not in ignore]
    BEASTFILE.write_text(json.dumps({beast.title: beast.as_dict() for beast in beasts}, indent=2))
    log.info("%i beasts written to %s", len(beasts), BEASTFILE)
