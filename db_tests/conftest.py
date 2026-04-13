from uuid import uuid4
import pytest
from db_tests.db_client import DBClient
from utils.logging_config import setup_logger

logger = setup_logger("db_tests")


@pytest.fixture
def db_client():
    client = DBClient()
    yield client
    client.close()


@pytest.fixture
def user_email():
    return f"test_{uuid4()}@test.com"


@pytest.hookimpl(trylast=True)
def pytest_runtest_logreport(report):
    if report.when != "call":
        return
    if report.passed:
        logger.info("PASSED %s", report.nodeid)
    elif report.failed:
        logger.error("FAILED %s", report.nodeid)
        logger.error("%s", report.longrepr)