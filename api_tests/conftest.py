import pytest
from faker import Faker
from api_tests.client.api_client import ApiClient
from api_tests.endpoints import BASE_URL
from api_tests.services.users_service import UsersService
from utils.logging_config import setup_logger


fake = Faker()
logger = setup_logger("api_tests")


@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)


@pytest.fixture
def users_service(api_client):
    return UsersService(api_client)


@pytest.fixture
def user_data():
    return {
        "name": fake.name(),
        "job": fake.job()
    }


@pytest.hookimpl(trylast=True)
def pytest_runtest_logreport(report):
    if report.when != "call":
        return
    if report.passed:
        logger.info("PASSED %s", report.nodeid)
    elif report.failed:
        logger.error("FAILED %s", report.nodeid)
        logger.error("%s", report.longrepr)