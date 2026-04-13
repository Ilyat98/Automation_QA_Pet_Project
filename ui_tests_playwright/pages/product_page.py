import math
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """
    def add_product_to_basket(self):
        self.wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET_BUTTON)).click()
        self.solve_quiz_and_get_code()


    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
        except NoAlertPresentException:
            print("No quiz alert presented")
            return

        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented") """

    def add_product_to_basket(self):
        def handle_dialog(dialog):
            self.solve_quiz_and_get_code(dialog)
        self.page.on("dialog", handle_dialog)
        self.page.locator(ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def solve_quiz_and_get_code(self, dialog):
        alert_text = dialog.message
        x = alert_text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        dialog.accept(answer)
        try:
            second_dialog = self.page.wait_for_event("dialog", timeout=3000)
            print(f"Your code: {second_dialog.message}")
            second_dialog.accept()
        except:
            print("No second alert presented")

    def should_be_correct_product_name(self):
        product_name = self.page.locator(ProductPageLocators.PRODUCT_NAME).text_content()
        success_message = self.page.locator(ProductPageLocators.SUCCESS_MESSAGE).first.text_content()
        assert product_name == success_message, "Product name in message is incorrect"


    def should_be_correct_price(self):
        product_price = self.page.locator(ProductPageLocators.PRODUCT_PRICE).inner_text()
        basket_price = self.page.locator(ProductPageLocators.BASKET_PRICE).inner_text()
        assert product_price == basket_price, f"Basket price ({basket_price}) is different from product price ({product_price})"

    def should_not_be_success_message(self):
        success_messages = self.page.locator(ProductPageLocators.SUCCESS_MESSAGE)
        assert success_messages.count() == 0, "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        try:
            self.page.locator(ProductPageLocators.SUCCESS_MESSAGE).wait_for(state="hidden", timeout=5000)
        except:
            assert False, "Success message did not disappear"
