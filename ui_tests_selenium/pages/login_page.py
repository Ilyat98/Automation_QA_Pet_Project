import allure
from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):
    @allure.step("Verify login page is correct")
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    @allure.step("Check login form is present")
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form has not been found"

    @allure.step("Check register form is present")
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form has not been found"

    @allure.step("Register user with email: {email}")
    def register_user(self, email, password):
        self.should_be_register_form()
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.REGISTER_FORM_LINE_MAIL)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.REGISTER_FORM_LINE_PASS)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.REGISTER_FORM_LINE_PASS_CONFIRM)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_FORM_BUTTON)).click()

    @allure.step("Check registration error is displayed")
    def should_be_register_error(self):
        error = self.wait.until(EC.visibility_of_element_located(LoginPageLocators.REGISTER_ERROR_MESSAGE))
        assert error is not None, "Registration error message is not displayed"
