from config.config import BASE_URL
from ui_tests_playwright.pages.basket_page import BasketPage
from ui_tests_playwright.pages.main_page import MainPage


class TestBasketPage:

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, page):
        main_page = MainPage(page, BASE_URL)
        main_page.open()
        main_page.go_to_basket_page()
        basket_page = BasketPage(page, page.url)
        basket_page.should_be_message_of_empty_basket()
        basket_page.should_not_be_list_of_products()