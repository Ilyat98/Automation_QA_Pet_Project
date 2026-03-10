import faker
import pytest
from conftest import browser
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from config.config import BASE_URL, PRODUCT_URL_1, PRODUCT_URL_2



@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = BASE_URL
        register_page = LoginPage(browser, link)
        register_page.open()
        register_page.go_to_login_page()
        self.email, self.password = register_page.register_random_user()


    def test_user_cant_see_success_message(self, browser):
        link = PRODUCT_URL_1
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()


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

    def test_guest_can_add_product_to_basket(self, browser):
        link = PRODUCT_URL_1
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_correct_product_name()
        page.should_be_correct_price()


    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = PRODUCT_URL_2
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = PRODUCT_URL_1
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()


    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = PRODUCT_URL_2
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


