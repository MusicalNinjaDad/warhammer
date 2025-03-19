from pathlib import Path

import pytest
from requests_file import FileAdapter

import warhammer_bestiary.scraper


def pytest_collection(session: pytest.Session) -> None:  # noqa: ARG001
    """Patch scraper request.session and site root before collection. Patches are needed for parametrization."""
    print(f"Siteroot was: {warhammer_bestiary.scraper.URI_ROOT}")
    warhammer_bestiary.scraper.session.mount("file://", FileAdapter())
    warhammer_bestiary.scraper.URI_ROOT = f"file://{Path().absolute()}" 
    print(f"Siteroot is now: {warhammer_bestiary.scraper.URI_ROOT}")