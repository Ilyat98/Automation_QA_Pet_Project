import math
import allure
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC




class ProductPage(BasePage):
    def _get_visible_text(self, locator, attempts=3):
        for attempt in range(attempts):
            try:
                return self.wait.until(EC.visibility_of_element_located(locator)).text
            except StaleElementReferenceException:
                if attempt == attempts - 1:
                    raise
        return ""

    @allure.step("Add product to basket")
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
            print("No second alert presented")


    def should_be_correct_product_name(self):
        product_name = self._get_visible_text(ProductPageLocators.PRODUCT_NAME)
        success_message = self._get_visible_text(ProductPageLocators.SUCCESS_MESSAGE)
        assert product_name == success_message, "Product name in message is incorrect"


    @allure.step("Check product price is correct")
    def should_be_correct_price(self):
        product_price = self._get_visible_text(ProductPageLocators.PRODUCT_PRICE)
        basket_price = self._get_visible_text(ProductPageLocators.BASKET_PRICE)
        assert product_price == basket_price, "Basket price is different from product price"


    @allure.step("Check success message is displayed")
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def success_message_should_be_disappeared(self, timeout=5):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout=timeout), \
            "Success message is presented, but should not be"