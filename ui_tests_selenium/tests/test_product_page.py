import time

import allure
import pytest
from ui_tests_selenium.pages.login_page import LoginPage
from ui_tests_selenium.pages.basket_page import BasketPage
from ui_tests_selenium.pages.product_page import ProductPage
from config.config import BASE_URL, PRODUCT_URL_1, PROMO_OFFER_LINK, PRODUCT_URL_2



@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, generate_login_data):
        link = BASE_URL
        register_page = LoginPage(browser, link)
        register_page.open()
        register_page.go_to_login_page()
        email, password = generate_login_data
        register_page.register_user(email, password)
        register_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = PRODUCT_URL_1
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()


    @allure.story("Add product to basket")
    def test_user_can_add_product_to_basket(self, browser):
        link = PRODUCT_URL_1
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.add_product_to_basket()
        page.should_be_correct_product_name()
        page.should_be_correct_price()


@pytest.mark.guest_user
class TestGuestAddToBasketFromProductPage:

    @pytest.mark.parametrize('promo_offer', [ 0, 1, 2, 3, 4, 5,
            pytest.param(7, marks=pytest.mark.xfail(reason="known bug")), 8, 9 ] )
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"{PROMO_OFFER_LINK}{promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_correct_product_name()
        page.should_be_correct_price()


    @allure.feature("Login")
    @allure.story("Guest can open login page")
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = PRODUCT_URL_2
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = PRODUCT_URL_1
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_message_of_empty_basket()
        basket_page.should_not_be_list_of_products()


    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = PRODUCT_URL_2
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


