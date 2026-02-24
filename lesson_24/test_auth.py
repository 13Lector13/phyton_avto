import requests
import logging
import os

BASE_URL = "http://127.0.0.1:8080"

log_path = os.path.join(os.path.dirname(__file__), "test_search.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path, mode="w"),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger(__name__)


def test_login_success():
    logger.info("POST /auth | user: test_user | expecting: 200")
    r = requests.post(f"{BASE_URL}/auth", auth=("test_user", "test_pass"))
    logger.info(f"Response: {r.status_code}")
    assert r.status_code == 200
    response = r.json()
    assert response["access_token"]


def test_login_unsuccess():
    logger.info("POST /auth | user: user | expecting: 401")
    r = requests.post(f"{BASE_URL}/auth", auth=("user", "pass"))
    logger.info(f"Response: {r.status_code}")
    assert r.status_code == 401


def test_login_not_allowed_method():
    logger.info("GET /auth | wrong method | expecting: 405")
    r = requests.get(f"{BASE_URL}/auth", auth=("test_user", "test_pass"))
    logger.info(f"Response: {r.status_code}")
    assert r.status_code == 405