from pathlib import Path
from typing import Protocol

import pytest
import requests
from assets.statblocks import StatBlockTestCase, amoeba, soldiers, thugs

from warhammer_bestiary.scraper import WikiPage
from warhammer_bestiary.statblocks import generate_class


class PageParam(Protocol):
    param: Path


@pytest.fixture
def page(request: PageParam, requests_session: requests.Session) -> WikiPage:
    uri = request.param
    return WikiPage(uri=f"file://{uri}", session=requests_session)


parametrized = pytest.mark.parametrize(
    ["page", "stats"],
    [
        pytest.param(
            Path("tests/assets/amoeba.html").absolute(),
            amoeba.stats,
            id="Amoeba",
        ),
        pytest.param(
            Path("tests/assets/bat.html").absolute(),
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
            Path("tests/assets/NPC-artisans_apprentice.html").absolute(),
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
        pytest.param(
            Path("tests/assets/thugs.html").absolute(),
            thugs.stats,
            id="Thugs",
        ),
        pytest.param(
            Path("tests/assets/soldiers.html").absolute(),
            soldiers.stats,
            id="Soldiers",
        ),
    ],
    indirect=["page"],
)


@parametrized
def test_numstatblocks(page: WikiPage, stats: dict):
    assert len(page.statblocks) == sum(len(group) for group in stats.values())


@parametrized
def test_pagetitle(page: WikiPage, stats, request: pytest.FixtureRequest):  # noqa: ARG001
    """Should match test id."""
    assert page.title == request.node.callspec.id


@parametrized
def test_statblocks(page: WikiPage, stats):
    assert page.as_dict() == stats


@pytest.mark.parametrize(
    "beast",
    [amoeba, thugs, soldiers],
    ids=lambda beast: beast.beast,
)
def test_generate_py(beast: StatBlockTestCase):
    assert generate_class(beast.beast, beast.stats) == beast.statblock_class
