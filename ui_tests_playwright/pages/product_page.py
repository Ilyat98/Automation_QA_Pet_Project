from playwright.sync_api import expect
import math

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.page.click(ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):

        def handle_dialog(dialog):
            text = dialog.message
            x = text.split(" ")[2]
            answer = str(math.log(abs(12 * math.sin(float(x)))))
            dialog.accept(answer)

        self.page.on("dialog", handle_dialog)
        self.page.click(ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def should_be_correct_product_name(self):
        success_message = self.page.locator(ProductPageLocators.SUCCESS_MESSAGE)
        expect(success_message).to_be_visible()
        product_name_text = self.page.locator(ProductPageLocators.PRODUCT_NAME).text_content()
        expect(self.page.locator(ProductPageLocators.SUCCESS_MESSAGE)).to_have_text(product_name_text)

    def should_be_correct_price(self):
        product_price = self.page.locator(ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.page.locator(ProductPageLocators.BASKET_PRICE)

        expect(basket_price).to_be_visible()
        expect(basket_price).to_have_text(product_price.text_content())

    def should_not_be_success_message(self):
        expect(self.page.locator(ProductPageLocators.SUCCESS_MESSAGE)).not_to_be_visible()

    def success_message_should_be_disappeared(self):
        expect(self.page.locator(ProductPageLocators.SUCCESS_MESSAGE)).to_be_hidden()