from playwright.sync_api import expect
from ui_tests_playwright.pages.base_page import BasePage
from ui_tests_playwright.pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.page.url, "Login page URL is incorrect"

    def should_be_login_form(self):
        assert self.page.locator(LoginPageLocators.LOGIN_FORM).is_visible(), \
            "Login form has not been found"

    def should_be_register_form(self):
        assert self.page.locator(LoginPageLocators.REGISTER_FORM).is_visible(), \
            "Register form has not been found"

    def register_user(self, email, password):
        self.should_be_register_form()
        self.page.locator(LoginPageLocators.REGISTER_FORM_LINE_MAIL).fill(email)
        self.page.locator(LoginPageLocators.REGISTER_FORM_LINE_PASS).fill(password)
        self.page.locator(LoginPageLocators.REGISTER_FORM_LINE_PASS_CONFIRM).fill(password)
        self.page.locator(LoginPageLocators.REGISTER_FORM_BUTTON).click()

    def should_be_register_error(self):
        assert self.page.locator(LoginPageLocators.REGISTER_ERROR_MESSAGE).is_visible(), \
            "Registration error message is not displayed"


