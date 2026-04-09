import allure

from ui_tests_playwright.pages.locators import BasePageLocators
from playwright.sync_api import expect

class BasePage:

    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    @allure.step("Go to login page")
    def go_to_login_page(self):
        self.page.locator(BasePageLocators.LOGIN_LINK).click()

    def go_to_basket_page(self):
        self.page.locator(BasePageLocators.BASKET_BUTTON_LINK).click()

    def should_be_element_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def get_current_url(self):
        return self.page.url