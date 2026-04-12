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

    def should_be_login_link(self):
        assert self.page.locator(BasePageLocators.LOGIN_LINK).is_visible(), \
            "Login link is not presented"

    def is_element_present(self, locator):
        return self.page.locator(locator).is_visible()

    def is_not_element_present(self, locator):
        return self.page.locator(locator).count() == 0

    def is_disappeared(self, locator):
        try:
            self.page.locator(locator).wait_for(state="hidden", timeout=4000)
            return True
        except:
            return False

    def should_be_authorized_user(self):
        assert self.page.locator(BasePageLocators.USER_ICON).is_visible(), \
            "User icon is not presented, probably unauthorised user"
