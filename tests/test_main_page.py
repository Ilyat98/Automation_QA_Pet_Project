import pytest
from config.config import Login_PAGE_URL, BASE_URL
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage



@pytest.mark.login_guest
class TestGuestLoginFromMainPage:

    def test_guest_should_see_login_link(self, browser):
        link = Login_PAGE_URL
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_should_see_login_page(self, browser):
        page = MainPage(browser, BASE_URL)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = BASE_URL
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_be_message_of_empty_basket()
        page.should_not_be_list_of_products()






