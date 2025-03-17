from pathlib import Path

import pytest
import requests
from bs4 import BeautifulSoup
from requests_file import FileAdapter

from warhammer_bestiary import Beast, get_and_parse


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

def test_get_statblocks(amoeba: BeautifulSoup):
    statblocks = Beast.get_statblocks(amoeba)
    assert len(statblocks) == 1

def test_parse_block(amoeba: BeautifulSoup):
    statblock = Beast.get_statblocks(amoeba)[0]
    assert Beast.parse_statblock(statblock) == {
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
    }

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
    ],
    indirect=["soup"],
)

@parametrized
def test_get_stats(soup: BeautifulSoup, pageclass: type, stats):
    assert pageclass.get_stats(soup) == stats
    