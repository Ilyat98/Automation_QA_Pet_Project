import allure
import pytest
from api_tests.conftest import fake
from config.config import BASE_URL
from ui_tests_selenium.pages.login_page import LoginPage
from ui_tests_selenium.pages.main_page import MainPage



@allure.feature("Authentication")
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

    @allure.story("Negative registration")
    @pytest.mark.negative
    def test_user_cant_register_with_invalid_email(self, browser):
        page = LoginPage(browser, BASE_URL)
        page.open()
        page.go_to_login_page()
        email = "invalid@test"
        password = fake.password(length=12, special_chars=True)
        page.register_user(email, password)
        page.should_be_register_error()

    @allure.story("Negative registration")
    @pytest.mark.negative
    def test_user_cant_register_with_short_password(self, browser):
        page = LoginPage(browser, BASE_URL)
        page.open()
        page.go_to_login_page()
        email = fake.email()
        password = fake.password(length=3, special_chars=False)
        page.register_user(email, password)
        page.should_be_register_error()