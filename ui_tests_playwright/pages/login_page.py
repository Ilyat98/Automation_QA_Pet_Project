from playwright.sync_api import expect
from ui_tests_playwright.pages.base_page import BasePage
from ui_tests_playwright.pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_form(self):
        expect(self.page.locator(LoginPageLocators.LOGIN_FORM)).to_be_visible()

    def should_be_register_form(self):
        expect(self.page.locator(LoginPageLocators.REGISTER_FORM)).to_be_visible()

    def register_random_user(self, email, password):

        self.page.fill(LoginPageLocators.REGISTER_FORM_LINE_MAIL, email)
        self.page.fill(LoginPageLocators.REGISTER_FORM_LINE_PASS, password)
        self.page.fill(LoginPageLocators.REGISTER_FORM_LINE_PASS_CONFIRM, password)

        self.page.click(LoginPageLocators.REGISTER_FORM_BUTTON)

