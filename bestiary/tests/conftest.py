import pytest
import requests
from requests_file import FileAdapter


@pytest.fixture(scope="module")
def requests_session() -> requests.Session:
    """Provide a `requests.Session` with `FileAdaptor`  and module-scoped cache."""
    session = requests.Session()
    session.mount("file://", FileAdapter())
    return session