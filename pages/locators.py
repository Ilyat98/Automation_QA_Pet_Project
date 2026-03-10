from selenium.webdriver.common.by import By




class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_LINK = (By.CSS_SELECTOR, "span .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_LINE_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_LINE_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_LINE_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class BasketPageLocators:
    MESSAGE_OF_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    LIST_OF_PRODUCTS = (By.CSS_SELECTOR, ".basket_summary #basket_formset")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")