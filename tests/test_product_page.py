import time
import pytest
from conftest import browser
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import faker


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/uk/"
        fake_data = faker.Faker()
        paswrd = fake_data.password()
        mail = fake_data.email()
        register_page = LoginPage(browser, link)
        register_page.open()
        register_page.go_to_login_page()
        print(mail)
        print(paswrd)
        register_page.register_new_user(mail, paswrd)



    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.add_product_to_basket()
        page.should_be_correct_product_name()
        page.should_be_correct_price()


@pytest.mark.need_review
@pytest.mark.parametrize("promo_offer",[0,1,2,3,4,5,6,
        pytest.param(7, marks=pytest.mark.xfail(reason="wrong_link")),8,9])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_correct_product_name()
    page.should_be_correct_price()


@pytest.mark.xfail
@pytest.mark.parametrize('promo_offer', range(0,9))
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('promo_offer', range(0,9))
def test_guest_cant_see_success_message(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('promo_offer', range(0,9))
def test_message_disappeared_after_adding_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_be_disappeared()


@pytest.mark.parametrize('promo_offer', range(0,9))
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_message_of_empty_basket()
    page.should_not_be_list_of_products()



