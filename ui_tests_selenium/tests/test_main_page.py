import pytest
import allure

from config.config import BASE_URL, Login_PAGE_URL
from ui_tests_selenium.pages.login_page import LoginPage
from ui_tests_selenium.pages.main_page import MainPage
from ui_tests_selenium.pages.basket_page import BasketPage



@pytest.mark.login_guest
@allure.feature("UI Selenium - Main")
@allure.story("Guest navigation from main page")
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
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_message_of_empty_basket()
        basket_page.should_not_be_list_of_products()






