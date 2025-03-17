"""Scrap StatBlocks from https://wfrp1e.fandom.com/wiki/Category:Bestiary and save to file."""

import json
import logging
from pathlib import Path
from typing import Final

import requests
from bs4 import BeautifulSoup

URI_ROOT = "https://wfrp1e.fandom.com"

BEASTIARY_STARTING_PAGE = "/wiki/Category:Bestiary"

OUTPUT_FILE = Path("beasts.json")
LOG_FILE = Path("beasts.log")

log = logging.getLogger("BeastScraper")
logfile = logging.FileHandler(LOG_FILE)
logfile.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
logfile.setFormatter(formatter)
log.addHandler(logfile)
log.setLevel(logging.INFO)

session = requests.Session()

def get_and_parse(uri: str, uri_root: str = URI_ROOT, session: requests.Session = session) -> BeautifulSoup:  # noqa: D103
    full_uri = f"{uri_root}{uri}"
    _raw = session.get(full_uri, timeout=10)
    log.debug("Parsing %s", full_uri)
    return BeautifulSoup(_raw.text, features="html.parser")

class Beast:
    """A page for a normal member of the bestiary, with the stat block shown vertically at the side of the page."""

    @classmethod
    def get_statblocks(cls, page: BeautifulSoup) -> list[BeautifulSoup]:
        """Statblocks are in an `aside` tag with class `type-stat`."""
        log.debug("Getting statblocks for: %s", page)
        return page.find_all(class_="type-stat")

    @classmethod
    def parse_statblock(cls, block: BeautifulSoup) -> dict[str, int]:
        """Stat value is tagged with class `pi-data`and `data-source` attribute showing the stat name."""
        log.debug("Parsing statblock %s", block)
        stats = block.find_all(class_="pi-data")
        log.debug("Found %i statblocks", len(stats))
        
        def parse_stat(div: BeautifulSoup) -> int:
            """Handle cases where values may be missing or given as dice rolls etc."""
            log.debug("Parsing Stat: %s", div)
            stat = div.find(class_="pi-data-value").contents[0]
            if div.find(class_="pi-data-value").contents[0] == "-":
                val = 0
            else:
                try:
                    val = int(stat)
                except TypeError as e:
                    # This occurs if `-` was identified as an empty `<ul>`
                    log.error("TypeError %s when parsing %s", e, div)  # noqa: TRY400
                    val = 0
                except ValueError as e:
                    # E.g. "d6" or "3-5"
                    log.error("ValueError %s when parsing %s", e, div)  # noqa: TRY400
                    val = str(stat)
            return val
        
        return {stat["data-source"]: parse_stat(stat) for stat in stats}

    @classmethod
    def get_stats(cls, page: BeautifulSoup) -> dict[str, dict[str, int]]:
        """Stat block title is in a `h2` block of class `pi-header`."""
        return {
            block.find(class_="pi-header").contents[0]: cls.parse_statblock(block) for block in cls.get_statblocks(page)
        }

class NPC:
    """NPCs have stat blocks in a horizontal table in the text."""

    STARTING_PAGE: Final = "/wiki/Category:NPCs"

    @classmethod
    def get_statblocks(cls, page: BeautifulSoup) -> list[BeautifulSoup]:
        """Stat Blocks are in tables of class `article-table`."""
        log.debug("Getting statblocks for: %s", page.find("title").contents)
        return page.find_all("table", class_="article-table")
    
    @classmethod
    def parse_statblock(cls, block: BeautifulSoup) -> dict[str, int]:
        """No tags - need to parse table."""
        log.debug("Parsing statblock %s", block)
        
        def parse_stat(value: str) -> int:
            """Handle cases where values may be missing or given as dice rolls etc."""
            log.debug("Parsing Stat: %s", value)
            if value == "-":
                val = 0
            else:
                try:
                    val = int(value)
                except TypeError as e:
                    # This occurs if `-` was identified as an empty `<ul>`
                    log.error("TypeError %s when parsing %s", e, value)  # noqa: TRY400
                    val = 0
                except ValueError as e:
                    # E.g. "d6" or "3-5"
                    log.error("ValueError %s when parsing %s", e, value)  # noqa: TRY400
                    val = str(value)
            return val
        
        table = [list(row.strings) for row in block.find_all("tr")]

        return {
            statname: parse_stat(statvalue)
            for statname, statvalue in zip(table[0], table[1], strict=True)
            if statname != "\n"
        }
    
    @classmethod
    def get_stats(cls, page: BeautifulSoup) -> dict[str, dict[str, int]]:
        """No stat block title."""
        blocks = cls.get_statblocks(page)
        if len(blocks) > 1:
            log.error("Too many statblocks (%i) for %s", len(blocks), page.find("title").string)
        return {"Basic Profile": cls.parse_statblock(blocks[0])}


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
