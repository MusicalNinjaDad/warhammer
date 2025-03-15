import pickle
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from warhammer_bestiary import get_statblocks, get_stats, parse_statblock


@pytest.fixture
def amoeba() -> BeautifulSoup:
    pickled_file = Path("tests/assets/amoeba.pkl")
    with pickled_file.open("rb") as pickled:
        page = pickle.load(pickled)  # noqa: S301
    return page  # noqa: RET504

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
    