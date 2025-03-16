from pathlib import Path

import pytest
import requests
from bs4 import BeautifulSoup
from requests_file import FileAdapter

from warhammer_bestiary import get_statblocks, get_stats, parse_statblock
from warhammer_bestiary.scraper import get_and_parse


@pytest.fixture(scope="session")
def requests_session() -> requests.Session:
    session = requests.Session()
    session.mount("file://", FileAdapter())
    return session

@pytest.fixture
def amoeba(requests_session: requests.Session) -> BeautifulSoup:
    localcopy = Path("tests/assets/amoeba.html").resolve()
    return get_and_parse(str(localcopy), uri_root="file://", session=requests_session)

def test_get_statblocks(amoeba: BeautifulSoup):
    statblocks = get_statblocks(amoeba)
    assert len(statblocks) == 1

def test_parse_block(amoeba: BeautifulSoup):
    statblock = get_statblocks(amoeba)[0]
    assert parse_statblock(statblock) == {
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

def test_get_stats(amoeba: BeautifulSoup):
    assert get_stats(amoeba) == {
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
    }
    