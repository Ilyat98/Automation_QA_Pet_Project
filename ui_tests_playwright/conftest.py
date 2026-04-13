import pytest
from faker import Faker
from utils.logging_config import setup_logger

fake = Faker()
logger = setup_logger("ui_playwright")

@pytest.fixture
def generate_login_data():
    fake_email = fake.email()
    fake_pass = fake.password(9)
    return fake_email, fake_pass


@pytest.hookimpl(trylast=True)
def pytest_runtest_logreport(report):
    if report.when != "call":
        return
    if report.passed:
        logger.info("PASSED %s", report.nodeid)
    elif report.failed:
        logger.error("FAILED %s", report.nodeid)
        logger.error("%s", report.longrepr)