ADD_TO_BASKET = ".btn-add-to-basket"
PRODUCT_NAME = ".product_main h1"
SUCCESS_MESSAGE = ".alert-success strong"


class BasePageLocators:
    LOGIN_LINK = "#login_link"
    LOGIN_LINK_INVALID = "#login_link_inc"
    BASKET_BUTTON_LINK = ".btn-group a.btn"
    USER_ICON = ".icon-user"


class MainPageLocators:
    LOGIN_LINK = "#login_link"


class LoginPageLocators:
    LOGIN_FORM = "#login_form"
    REGISTER_FORM = "#register_form"
    REGISTER_FORM_LINE_MAIL = "#id_registration-email"
    REGISTER_FORM_LINE_PASS = "#id_registration-password1"
    REGISTER_FORM_LINE_PASS_CONFIRM = "#id_registration-password2"
    REGISTER_FORM_BUTTON = "[name='registration_submit']"
    REGISTER_ERROR_MESSAGE = ".alert-danger"


class BasketPageLocators:
    MESSAGE_OF_EMPTY_BASKET = "#content_inner p"
    LIST_OF_PRODUCTS = ".basket_summary #basket_formset"


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = ".btn-add-to-basket"
    PRODUCT_NAME = ".product_main h1"
    PRODUCT_PRICE = "p.price_color"
    SUCCESS_MESSAGE = ".alert-success strong"
    BASKET_PRICE = ".alert-info strong"