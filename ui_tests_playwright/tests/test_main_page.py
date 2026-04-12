import pytest
from config.config import Login_PAGE_URL, BASE_URL
from ui_tests_playwright.pages.basket_page import BasketPage
from ui_tests_playwright.pages.login_page import LoginPage
from ui_tests_playwright.pages.main_page import MainPage


@pytest.mark.login_guest
class TestGuestLoginFromMainPage:

    def test_guest_should_see_login_link(self, page):
        main_page = MainPage(page, Login_PAGE_URL)
        main_page.open()
        main_page.should_be_login_link()


    def test_guest_should_see_login_page(self, page):
        main_page = MainPage(page, BASE_URL)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(page, page.url)
        login_page.should_be_login_page()

    @pytest.mark.new
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, page):
        main_page = MainPage(page, BASE_URL)
        main_page.open()
        main_page.go_to_basket_page()
        basket_page = BasketPage(page, page.url)
        basket_page.should_be_message_of_empty_basket()
        basket_page.should_not_be_list_of_products()






