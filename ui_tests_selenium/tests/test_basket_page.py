from ui_tests_selenium.pages.main_page import MainPage
from ui_tests_selenium.pages.basket_page import BasketPage
from ui_tests_selenium.config.config import BASE_URL


class TestBasketPage:

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, BASE_URL)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_message_of_empty_basket()
        basket_page.should_not_be_list_of_products()