from pathlib import Path
from typing import Protocol

import pytest
import requests
from assets.statblocks import StatBlockTestCase, amoeba, artisans_apprentice, bat, soldiers, thugs

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
            bat.stats,
            id="Bat",
        ),
        pytest.param(
            Path("tests/assets/NPC-artisans_apprentice.html").absolute(),
            artisans_apprentice.stats,
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
