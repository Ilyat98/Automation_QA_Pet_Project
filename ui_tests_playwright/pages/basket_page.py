from playwright.sync_api import expect
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_of_empty_basket(self):
        expect(self.page.locator(BasketPageLocators.MESSAGE_OF_EMPTY_BASKET)).to_be_visible()

    def should_not_be_list_of_products(self):
        expect(self.page.locator(BasketPageLocators.LIST_OF_PRODUCTS)).to_have_count(0)