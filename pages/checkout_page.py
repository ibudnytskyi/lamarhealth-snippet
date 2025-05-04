from pages.base_page import BasePage
from locators.page_locators import CheckoutPageLocators, CartPageLocators


class CartPage(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.locators = CartPageLocators()

    def proceed_to_checkout(self):
        self.logger.info("Proceeding to checkout")
        self.click_element(self.locators.CHECKOUT_BUTTON)


class CheckoutPage(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.locators = CheckoutPageLocators()

    def fill_checkout_form(self, first_name=None, last_name=None, postal_code=None):
        if first_name:
            self.fill_field(self.locators.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.fill_field(self.locators.LAST_NAME_INPUT, last_name)
        if postal_code:
            self.fill_field(self.locators.POSTAL_CODE_INPUT, postal_code)

    def continue_checkout(self):
        self.logger.info("Continuing checkout process")
        self.click_element(self.locators.CONTINUE_BUTTON)

    def get_error_message(self):
        if self.is_visible(self.locators.ERROR_MESSAGE):
            error_msg = self.get_text(self.locators.ERROR_MESSAGE)
            self.logger.warning(f"Checkout validation error: {error_msg}")
            return error_msg
        return None