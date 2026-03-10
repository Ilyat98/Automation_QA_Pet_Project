from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(self, browser):
    link = BASE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()