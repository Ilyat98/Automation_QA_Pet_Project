import allure
import pytest

from config.config import BASE_URL
from ui_tests_playwright.conftest import fake
from ui_tests_playwright.pages.login_page import LoginPage
from ui_tests_playwright.pages.main_page import MainPage


class TestLoginPage:

    def test_guest_can_go_to_login_page(self, page):
        main_page = MainPage(page, BASE_URL)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(page, page.url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_form(self, page):
        link = f"{BASE_URL}accounts/login/"
        login_page = LoginPage(page, link)
        login_page.open()
        login_page.should_be_login_form()


    def test_guest_should_see_register_form(self, page):
        link = f"{BASE_URL}accounts/login/"
        login_page = LoginPage(page, link)
        login_page.open()
        login_page.should_be_register_form()

    def test_login_page_url_should_contain_login(self, page):
        link = f"{BASE_URL}accounts/login/"
        login_page = LoginPage(page, link)
        login_page.open()
        login_page.should_be_login_url()

    @allure.story("Negative registration")
    @pytest.mark.negative
    def test_user_cant_register_with_invalid_email(self, page):
        login_page = LoginPage(page, BASE_URL)
        login_page.open()
        login_page.go_to_login_page()
        email = "invalid@test"
        password = fake.password(length=12, special_chars=True)
        login_page.register_user(email, password)
        login_page.should_be_register_error()

    @allure.story("Negative registration")
    @pytest.mark.negative
    def test_user_cant_register_with_short_password(self, page):
        login_page = LoginPage(page, BASE_URL)
        login_page.open()
        login_page.go_to_login_page()
        email = fake.email()
        password = fake.password(length=3, special_chars=False)
        login_page.register_user(email, password)
        login_page.should_be_register_error()


