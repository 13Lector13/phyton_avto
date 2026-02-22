import requests
import pytest
import logging
# from requests.auth import HTTPBasicAuth
import os

BASE_URL = "http://127.0.0.1:8080"

log_path = os.path.join(os.path.dirname(__file__), "test_search.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def login():
    r = requests.post(f"{BASE_URL}/auth", auth=("test_user", "test_pass"))
    assert r.status_code == 200
    return r.json()["access_token"]


@pytest.mark.parametrize("sort_by,limit,expected_len", [
    ("price", 5, 5),
    ("year", 3, 3),
    ("brand", 10, 10),
    (None, 1, 1),
    ("engine_volume", 7, 7),
    ("price", None, 25),
    (None, None, 25),
])
class TestCars:

    def test_get_cars(self, login, sort_by, limit, expected_len):
        logger.info(f"GET /cars | params: sort_by={sort_by}, limit={limit}")

        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        r = requests.get(f"{BASE_URL}/cars", headers={"Authorization": f"Bearer {login}"}, params=params)

        logger.info(f"Response: {r.status_code} | items returned: {len(r.json())}")

        assert r.status_code == 200
        assert isinstance(r.json(), list)
        assert len(r.json()) == expected_len

        if sort_by:
            data = r.json()
            values = [car[sort_by] for car in data]
            assert values == sorted(values), f"Not sorted by {sort_by}"
