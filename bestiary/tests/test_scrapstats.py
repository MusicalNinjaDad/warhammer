from pathlib import Path

import pytest
import requests
from bs4 import BeautifulSoup
from requests_file import FileAdapter

from warhammer_bestiary import NPC, Beast, get_and_parse


@pytest.fixture(scope="session")
def requests_session() -> requests.Session:
    session = requests.Session()
    session.mount("file://", FileAdapter())
    return session

@pytest.fixture
def amoeba(requests_session: requests.Session) -> BeautifulSoup:
    localcopy = Path("tests/assets/amoeba.html").resolve()
    return get_and_parse(str(localcopy), uri_root="file://", session=requests_session)

@pytest.fixture
def soup(requests_session: requests.Session, request: pytest.FixtureRequest) -> BeautifulSoup:
    return get_and_parse(str(request.param), uri_root="file://", session=requests_session)

parametrized = pytest.mark.parametrize(
    ["soup", "pageclass", "stats"],
    [
        pytest.param(
            Path("tests/assets/amoeba.html").resolve(),
            Beast,
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
            Path("tests/assets/bat.html").resolve(),
            Beast,
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
            Path("tests/assets/NPC-artisans_apprentice.html").resolve(),
            NPC,
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
    indirect=["soup"],
)

@parametrized
def test_get_statblocks(soup: BeautifulSoup, pageclass: type, stats):
    statblocks = pageclass.get_statblocks(soup)
    assert len(statblocks) == len(stats)

@parametrized
def test_parse_block(soup: BeautifulSoup, pageclass: type, stats):
    statblock = pageclass.get_statblocks(soup)[0]
    assert pageclass.parse_statblock(statblock) == stats["Basic Profile"]


@parametrized
def test_get_stats(soup: BeautifulSoup, pageclass: type, stats):
    assert pageclass.get_stats(soup) == stats
