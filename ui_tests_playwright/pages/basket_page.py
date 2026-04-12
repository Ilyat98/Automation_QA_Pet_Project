from playwright.sync_api import expect
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_of_empty_basket(self):
        assert self.page.locator(BasketPageLocators.MESSAGE_OF_EMPTY_BASKET).is_visible(), \
            "Empty basket message is not presented"

    def should_not_be_list_of_products(self):
        assert self.page.locator(BasketPageLocators.LIST_OF_PRODUCTS).count() == 0, \
            "Products are present in basket, but should not be"