"""Scrap StatBlocks from https://wfrp1e.fandom.com/wiki/Category:Bestiary and save to file."""

import json
import logging
from pathlib import Path

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

def get_and_parse(uri: str) -> BeautifulSoup:  # noqa: D103
    full_uri = f"{URI_ROOT}{uri}"
    _raw = requests.get(full_uri, timeout=10)
    log.debug("Parsing %s", full_uri)
    return BeautifulSoup(_raw.text, features="html.parser")


def get_statblocks(page: BeautifulSoup) -> list[BeautifulSoup]:  # noqa: D103
    log.debug("Getting statblocks for: %s", page)
    return page.find_all(class_="type-stat")


def parse_statblock(block: BeautifulSoup) -> dict[str, int]:  # noqa: D103
    log.debug("Parsing statblock %s", block)
    stats = block.find_all(class_="pi-data")
    log.debug("Found %i statblocks", len(stats))
    
    def parse_stat(div: BeautifulSoup) -> int:
        log.debug("Parsing Stat: %s", div)
        stat = div.find(class_="pi-data-value").contents[0]
        if div.find(class_="pi-data-value").contents[0] == "-":
            val = 0
        else:
            try:
                val = int(stat)
            except (TypeError, ValueError) as e:
                log.error("Error %s when parsing %s", e, div)  # noqa: TRY400
                val = 0
        return val
    
    return {stat["data-source"]: parse_stat(stat) for stat in stats}


def get_stats(page: BeautifulSoup) -> dict[str, dict[str, int]]:  # noqa: D103
    return {block.find(class_="pi-header").contents[0]: parse_statblock(block) for block in get_statblocks(page)}


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
        log.info("Getting %s", beast) or beast: get_stats(beast_page)
        for beast, beast_page in beast_page_contents.items()
    }

    log.info("Got %i beasts", len(beasts))
    log.debug("Got: %r", beasts)

    OUTPUT_FILE.write_text(json.dumps(beasts))
    log.info("Written data to %s", OUTPUT_FILE)
