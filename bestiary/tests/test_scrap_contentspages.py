from pathlib import Path

import pytest
import requests

from wfrp.scraper import NPC, Beast, WikiPage


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
