from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_message_of_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_list_of_products(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_PRODUCTS), \
            "Success message is presented, but should not be"