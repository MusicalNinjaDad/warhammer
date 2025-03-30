from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import pytest
import requests
from requests_file import FileAdapter

from warhammer_bestiary.scraper import NPC, Beast, WikiPage
from warhammer_bestiary.statblocks import generate_class


class PageParam(Protocol):
    param: Path


@dataclass
class TestCase:
    beast: str
    stats: dict[str, int | str]
    statblock_class: list[str]


amoeba = TestCase(
    beast="Amoeba",
    stats={
        "": {
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
    },
    statblock_class=[
        "class Amoeba(Warhammer):",
        "    M = 4",
        "    WS = 33",
        "    BS = 0",
        "    S = 3",
        "    T = 5",
        "    W = 11",
        "    I = 30",
        "    A = 3",
        "    Dex = 0",
        "    Ld = 0",
        "    Int = 0",
        "    Cl = 0",
        "    WP = 0",
        "    Fel = 0",
        "",
    ],
)

thugs = TestCase(
    beast="Thugs",
    stats={
        "Thug": {
            "Basic Profile": {
                "M": 4,
                "WS": 31,
                "BS": 25,
                "S": 3,
                "T": 4,
                "W": 7,
                "I": 30,
                "A": 1,
                "Dex": 29,
                "Ld": 29,
                "Int": 29,
                "Cl": 29,
                "WP": 29,
                "Fel": 29,
            },
        },
        "Teamsters or Stevedores": {
            "Basic Profile": {
                "M": 4,
                "WS": 33,
                "BS": 25,
                "S": 3,
                "T": 4,
                "W": 8,
                "I": 30,
                "A": 1,
                "Dex": 34,
                "Ld": 28,
                "Int": 33,
                "Cl": 30,
                "WP": 32,
                "Fel": 29,
            },
        },
    },
    statblock_class=[
        "class Thugs:",
        "    class Thug(Warhammer):",
        "        M = 4",
        "        WS = 31",
        "        BS = 25",
        "        S = 3",
        "        T = 4",
        "        W = 7",
        "        I = 30",
        "        A = 1",
        "        Dex = 29",
        "        Ld = 29",
        "        Int = 29",
        "        Cl = 29",
        "        WP = 29",
        "        Fel = 29",
        "",
        "    class Teamsters_or_Stevedores(Warhammer):",
        "        M = 4",
        "        WS = 33",
        "        BS = 25",
        "        S = 3",
        "        T = 4",
        "        W = 8",
        "        I = 30",
        "        A = 1",
        "        Dex = 34",
        "        Ld = 28",
        "        Int = 33",
        "        Cl = 30",
        "        WP = 32",
        "        Fel = 29",
        "",
    ],
)


@pytest.fixture(scope="module")
def requests_session() -> requests.Session:
    """Provide a `requests.Session` with `FileAdaptor?  and module-scoped cache."""
    session = requests.Session()
    session.mount("file://", FileAdapter())
    return session


@pytest.fixture
def page(request: PageParam, requests_session: requests.Session) -> WikiPage:
    uri = request.param
    return WikiPage(uri=f"file://{uri}", session=requests_session)


@pytest.mark.parametrize(
    ["page_type", "contents_page", "num_links", "contains", "absent"],
    [
        pytest.param(
            Beast,
            Path("tests/assets/bestiary.html").absolute(),
            126,  # Thugs and High Elf Mage are not labeled with "(NPC)"
            ("Bat", "/wiki/Bat"),
            r"/wiki/Artisan%27s_Apprentice_(NPC)",
            id="Beastiary",
        ),
        pytest.param(
            NPC,
            Path("tests/assets/npcs.html").absolute(),
            38,
            ("Artisan's Apprentice (NPC)", r"/wiki/Artisan%27s_Apprentice_(NPC)"),
            "/wiki/Bat",
            id="NPC",
        ),
    ],
)
def test_get_page_uris(  # noqa: PLR0913
    page_type: type[WikiPage],
    contents_page: Path,
    num_links: int,
    contains: tuple[str, str],
    absent: str,
    requests_session: requests.Session,
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr(page_type, "CATEGORY_INDEX", f"file://{contents_page}", raising=True)
    links = page_type.get_page_uris(requests_session)
    assert len(links) == num_links
    assert contains in links.items()
    assert absent not in links.values()


def test_absolute():
    assert Beast.absolute("/wiki/Bat") == "https://wfrp1e.fandom.com/wiki/Bat"


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
            {
                "": {
                    "Generic Soldier": {
                        "M": 4,
                        "WS": 43,
                        "BS": 35,
                        "S": 3,
                        "T": 3,
                        "W": 8,
                        "I": 40,
                        "A": 1,
                        "Dex": 29,
                        "Ld": 39,
                        "Int": 29,
                        "Cl": 29,
                        "WP": 29,
                        "Fel": 29,
                    },
                },
                "The Imperial Guard": {
                    "Cavalry Officer": {
                        "M": 4,
                        "WS": 65,
                        "BS": 50,
                        "S": 5,
                        "T": 5,
                        "W": 13,
                        "I": 50,
                        "A": 3,
                        "Dex": 49,
                        "Ld": 69,
                        "Int": 39,
                        "Cl": 69,
                        "WP": 40,
                        "Fel": 50,
                    },
                    "Cavalryman": {
                        "M": 4,
                        "WS": 50,
                        "BS": 38,
                        "S": 4,
                        "T": 4,
                        "W": 11,
                        "I": 50,
                        "A": 3,
                        "Dex": 39,
                        "Ld": 39,
                        "Int": 29,
                        "Cl": 40,
                        "WP": 29,
                        "Fel": 30,
                    },
                    "Officer": {
                        "M": 4,
                        "WS": 60,
                        "BS": 45,
                        "S": 5,
                        "T": 5,
                        "W": 13,
                        "I": 60,
                        "A": 3,
                        "Dex": 49,
                        "Ld": 69,
                        "Int": 40,
                        "Cl": 60,
                        "WP": 40,
                        "Fel": 50,
                    },
                    "Soldier": {
                        "M": 4,
                        "WS": "50♦",
                        "BS": "40♦",
                        "S": 4,
                        "T": 4,
                        "W": 11,
                        "I": 50,
                        "A": 2,
                        "Dex": 39,
                        "Ld": 39,
                        "Int": 29,
                        "Cl": 40,
                        "WP": 29,
                        "Fel": 30,
                    },
                    "Mercenary Captain": {
                        "M": 4,
                        "WS": 55,
                        "BS": 45,
                        "S": 4,
                        "T": 4,
                        "W": 11,
                        "I": 55,
                        "A": 2,
                        "Dex": 39,
                        "Ld": 55,
                        "Int": 39,
                        "Cl": 50,
                        "WP": 35,
                        "Fel": 45,
                    },
                    "Mercenary Soldier": {
                        "M": 4,
                        "WS": 45,
                        "BS": 35,
                        "S": 3,
                        "T": 4,
                        "W": 8,
                        "I": 45,
                        "A": 2,
                        "Dex": 29,
                        "Ld": 39,
                        "Int": 29,
                        "Cl": 35,
                        "WP": 25,
                        "Fel": 30,
                    },
                    "Templar": {
                        "M": 4,
                        "WS": 70,
                        "BS": 55,
                        "S": 5,
                        "T": 5,
                        "W": 15,
                        "I": 70,
                        "A": 3,
                        "Dex": 59,
                        "Ld": 59,
                        "Int": 50,
                        "Cl": 65,
                        "WP": 60,
                        "Fel": 59,
                    },
                    "Halfling Infantry": {
                        "M": 3,
                        "WS": 38,
                        "BS": 45,
                        "S": 3,
                        "T": 3,
                        "W": 8,
                        "I": 60,
                        "A": 2,
                        "Dex": 49,
                        "Ld": 30,
                        "Int": 29,
                        "Cl": 34,
                        "WP": 55,
                        "Fel": 53,
                    },
                },
                "Standing Armies In The Empire": {
                    "Sergeant": {
                        "M": 4,
                        "WS": 50,
                        "BS": 30,
                        "S": 4,
                        "T": 4,
                        "W": 11,
                        "I": 50,
                        "A": 2,
                        "Dex": 39,
                        "Ld": 55,
                        "Int": 40,
                        "Cl": 50,
                        "WP": 35,
                        "Fel": 40,
                    },
                    "Soldier": {
                        "M": 4,
                        "WS": 45,
                        "BS": 30,
                        "S": 3,
                        "T": 3,
                        "W": 7,
                        "I": 40,
                        "A": 1,
                        "Dex": 29,
                        "Ld": 39,
                        "Int": 29,
                        "Cl": 29,
                        "WP": 25,
                        "Fel": 30,
                    },
                    "Pikeman": {
                        "M": 4,
                        "WS": 45,
                        "BS": 30,
                        "S": 3,
                        "T": 3,
                        "W": 7,
                        "I": 40,
                        "A": 1,
                        "Dex": 29,
                        "Ld": 40,
                        "Int": 29,
                        "Cl": 30,
                        "WP": 26,
                        "Fel": 29,
                    },
                    "Mercenary Crossbowman": {
                        "M": 4,
                        "WS": 40,
                        "BS": 50,
                        "S": 3,
                        "T": 4,
                        "W": 9,
                        "I": 45,
                        "A": 2,
                        "Dex": 39,
                        "Ld": 39,
                        "Int": 29,
                        "Cl": 35,
                        "WP": 30,
                        "Fel": 35,
                    },
                    "Gunnery Captain": {
                        "M": 4,
                        "WS": 54,
                        "BS": 30,
                        "S": 3,
                        "T": 3,
                        "W": 9,
                        "I": 45,
                        "A": 1,
                        "Dex": 29,
                        "Ld": 50,
                        "Int": 29,
                        "Cl": 30,
                        "WP": 26,
                        "Fel": 32,
                    },
                },
            },
            id="Soldiers",
        ),
    ],
    indirect=["page"],
)


@parametrized
def test_numstatblocks(page: WikiPage, stats):
    assert len(page.statblocks) == len(stats)


@parametrized
def test_pagetitle(page: WikiPage, stats, request: pytest.FixtureRequest):  # noqa: ARG001
    """Should match test id."""
    assert page.title == request.node.callspec.id


@parametrized
def test_parse_statblock(page: WikiPage, stats: dict[str, dict[str, int]]):
    statblock = page.statblocks[0]
    assert statblock.parse() == next(iter(stats.items()))


@parametrized
def test_statblocks(page: WikiPage, stats):
    assert page.as_dict() == stats


@pytest.mark.parametrize(
    "beast",
    [amoeba, thugs],
    ids=lambda beast: beast.beast,
)
def test_generate_py(beast: TestCase):
    assert generate_class(beast.beast, beast.stats) == beast.statblock_class
