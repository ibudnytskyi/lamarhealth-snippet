class LoginPageLocators:
    # XPath selectors using data-test attributes
    USERNAME_INPUT = '//input[@data-test="username"]'
    PASSWORD_INPUT = '//input[@data-test="password"]'
    LOGIN_BUTTON = '//input[@data-test="login-button"]'
    ERROR_MESSAGE = '//h3[@data-test="error"]'


class InventoryPageLocators:
    # XPath selectors for inventory page
    INVENTORY_ITEM = '//div[@class="inventory_item"]'
    ITEM_NAME = '.inventory_item_name'
    ITEM_PRICE = '.inventory_item_price'
    ITEM_DESCRIPTION = '.inventory_item_desc'
    SHOPPING_CART = '//a[@class="shopping_cart_link"]'

    # Most commonly used add button (for the first item)
    BACKPACK_ADD_BUTTON = '//button[@data-test="add-to-cart-sauce-labs-backpack"]'

    # Sort dropdown (for potential future use)
    SORT_DROPDOWN = '//select[@data-test="product_sort_container"]'


class CartPageLocators:
    # Buttons for cart operations
    CHECKOUT_BUTTON = '//button[@data-test="checkout"]'
    CONTINUE_SHOPPING_BUTTON = '//button[@data-test="continue-shopping"]'


class CheckoutPageLocators:
    # Step One: Customer Information
    FIRST_NAME_INPUT = '//input[@data-test="firstName"]'
    LAST_NAME_INPUT = '//input[@data-test="lastName"]'
    POSTAL_CODE_INPUT = '//input[@data-test="postalCode"]'
    CONTINUE_BUTTON = '//input[@data-test="continue"]'
    CANCEL_BUTTON = '//button[@data-test="cancel"]'
    ERROR_MESSAGE = '//h3[@data-test="error"]'

    # Step Two: Finish button for the checkout flow
    FINISH_BUTTON = '//button[@data-test="finish"]'

    # Complete Page
    BACK_HOME_BUTTON = '//button[@data-test="back-to-products"]'


class SideMenuLocators:
    # Core side menu elements
    BURGER_MENU_BUTTON = '//button[@id="react-burger-menu-btn"]'
    LOGOUT_LINK = '//a[@id="logout_sidebar_link"]'