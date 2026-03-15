import faker
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from .locators import LoginPageLocators, MainPageLocators
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form has not been found"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form has not been found"


    def register_random_user(self, generate_login_data):
        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_LINE_MAIL).send_keys(generate_login_data[0])
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_LINE_PASS).send_keys(generate_login_data[1])
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_LINE_PASS_CONFIRM).send_keys(generate_login_data[1])
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_FORM_BUTTON)).click()
