from pathlib import Path
from typing import Protocol

import pytest
import requests
from requests_file import FileAdapter

from warhammer_bestiary.scraper import NPC, Beast, WikiPage


class PageParam(Protocol):
    param: tuple[type[WikiPage], Path]


@pytest.fixture(scope="module")
def requests_session() -> requests.Session:
    """Provide a `requests.Session` with `FileAdaptor?  and module-scoped cache."""
    session = requests.Session()
    session.mount("file://", FileAdapter())
    return session


@pytest.fixture
def page(request: PageParam, requests_session: requests.Session) -> WikiPage:
    pagetype = request.param[0]
    uri = request.param[1]
    return pagetype(uri=f"file://{uri}", session=requests_session)


parametrized = pytest.mark.parametrize(
    ["page", "stats"],
    [
        pytest.param(
            (Beast, Path("tests/assets/amoeba.html").absolute()),
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
            id="Amoeba",
        ),
        pytest.param(
            (Beast, Path("tests/assets/bat.html").absolute()),
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
            id="Bat",
        ),
        pytest.param(
            (NPC, Path("tests/assets/NPC-artisans_apprentice.html").absolute()),
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
            id="Artisan's Apprentice (NPC)",
        ),
    ],
    indirect=["page"],
)


@parametrized
def test_statblocksoup(page: WikiPage, stats):
    statblocks = page.statblocksoup
    assert len(statblocks) == len(stats)


@parametrized
def test_pagetitle(page: WikiPage, stats, request: pytest.FixtureRequest):  # noqa: ARG001
    """Should match test id."""
    assert page.title == request.node.callspec.id


@parametrized
def test_parse_block(page: WikiPage, stats):
    statblock = page.statblocksoup[0]
    assert page.parse_statblock(statblock) == stats["Basic Profile"]


@parametrized
def test_get_stats(page: WikiPage, stats):
    assert page.stats == stats
