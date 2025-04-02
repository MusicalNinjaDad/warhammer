from pathlib import Path
from typing import Protocol

import pytest
import requests
from assets.statblocks import (
    StatBlockTestCase,
    amoeba,
    artisans_apprentice,
    bat,
    beast_of_nurgle,
    druidic_priest,
    horse,
    soldiers,
    thugs,
)

from warhammer_bestiary.scraper import WikiPage
from warhammer_bestiary.statblocks import generate_class


class PageParam(Protocol):
    param: Path


@pytest.fixture
def page(request: PageParam, requests_session: requests.Session) -> WikiPage:
    uri = request.param
    return WikiPage(uri=f"file://{uri}", session=requests_session)


parametrized = pytest.mark.parametrize(
    ["page", "beast"],
    [
        pytest.param(
            Path("tests/assets/amoeba.html").absolute(),
            amoeba,
            id="Amoeba",
        ),
        pytest.param(
            Path("tests/assets/bat.html").absolute(),
            bat,
            id="Bat",
        ),
        pytest.param(
            Path("tests/assets/NPC-artisans_apprentice.html").absolute(),
            artisans_apprentice,
            id="Artisan's Apprentice (NPC)",
        ),
        pytest.param(
            Path("tests/assets/thugs.html").absolute(),
            thugs,
            id="Thugs",
        ),
        pytest.param(
            Path("tests/assets/soldiers.html").absolute(),
            soldiers,
            id="Soldiers",
        ),
        pytest.param(
            Path("tests/assets/druidic_priest.html").absolute(),
            druidic_priest,
            id="Druidic Priest (Career)",
        ),
    ],
    indirect=["page"],
)


@parametrized
def test_numstatblocks(page: WikiPage, beast: StatBlockTestCase):
    assert len(page.statblocks) == sum(len(group) for group in beast.stats.values())


@parametrized
def test_pagetitle(page: WikiPage, beast: StatBlockTestCase):
    assert page.title == beast.beast


@parametrized
def test_statblocks(page: WikiPage, beast: StatBlockTestCase):
    assert page.as_dict() == beast.stats


@pytest.mark.parametrize(
    "beast",
    [amoeba, artisans_apprentice, beast_of_nurgle, horse, thugs, soldiers],
    ids=lambda beast: beast.beast,
)
def test_generate_py(beast: StatBlockTestCase):
    assert generate_class(beast.beast, beast.stats) == beast.statblock_class
