import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from utils.logging_config import setup_logger


SUPPORTED_BROWSERS = {"chrome", "firefox"}
fake = Faker()
logger = setup_logger("ui_selenium")


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Browser language")


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name not in SUPPORTED_BROWSERS:
        raise pytest.UsageError(f"--browser_name must be one of {SUPPORTED_BROWSERS}")

    if browser_name == "chrome":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})

        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", language)

        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service, options=options)

    browser.maximize_window()

    yield browser

    browser.quit()


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