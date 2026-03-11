import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import BASE_URL


@pytest.mark.login_guest
class TestLoginPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = BASE_URL
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_form(self, browser):
        link = f"{BASE_URL}accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()


    def test_guest_should_see_register_form(self, browser):
        link = f"{BASE_URL}accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_register_form()

    def test_login_page_url_should_contain_login(self, browser):
        link = f"{BASE_URL}accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_url()


