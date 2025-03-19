from pathlib import Path

import pytest
from requests_file import FileAdapter

import warhammer_bestiary.scraper
from warhammer_bestiary import NPC, Beast, WikiPage


def pytest_collection(session: pytest.Session) -> None:  # noqa: ARG001
    warhammer_bestiary.scraper.session.mount("file://", FileAdapter())
    warhammer_bestiary.scraper.URI_ROOT = f"file://{Path()}" 

parametrized = pytest.mark.parametrize(
    ["page", "stats"],
    [
        pytest.param(
            Beast("tests/assets/amoeba.html"),
            {
                "Basic Profile": {
                    "M": 4,
                    "WS": 33,
                    "BS": 0,
                    "S": 3,
                    "T": 5,
                    "W": 11,
                    "I": 30,
                    "A": 3,
                    "Dex": 0,
                    "Ld": 0,
                    "Int": 0,
                    "Cl": 0,
                    "WP": 0,
                    "Fel": 0,
                },
            },
            id="amoeba",
        ),
        pytest.param(
            Beast("tests/assets/bat.html"),
            {
                "Basic Profile": {
                    "M": 0,
                    "WS": 59,
                    "BS": 0,
                    "S": 0,
                    "T": 1,
                    "W": 1,
                    "I": 30,
                    "A": 1,
                    "Dex": 0,
                    "Ld": 14,
                    "Int": 5,
                    "Cl": 29,
                    "WP": 29,
                    "Fel": 0,
                },
            },
            id="bat",
        ),
        pytest.param(
            NPC("tests/assets/NPC-artisans_apprentice.html"),
            {
                "Basic Profile": {
                    "M": 4,
                    "WS": 31,
                    "BS": 25,
                    "S": 3,
                    "T": 3,
                    "W": 6,
                    "I": 40,
                    "A": 1,
                    "Dex": 39,
                    "Ld": 29,
                    "Int": 29,
                    "Cl": 29,
                    "WP": 29,
                    "Fel": 29,
                },
            },
            id="NPC",
        ),
    ],
)

@parametrized
def test_get_statblocks(page: WikiPage, stats):
    statblocks = page.statblocksoup
    assert len(statblocks) == len(stats)

@parametrized
def test_parse_block(page: WikiPage, stats):
    statblock = page.statblocksoup [0]
    assert page.parse_statblock(statblock) == stats["Basic Profile"]


@parametrized
def test_get_stats(page: WikiPage, stats):
    assert page.stats == stats
