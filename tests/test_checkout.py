from pages.inventory_page import InventoryPage
from pages.checkout_page import CartPage, CheckoutPage


class CheckoutTest:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.inventory_page = InventoryPage(page, logger)
        self.cart_page = CartPage(page, logger)
        self.checkout_page = CheckoutPage(page, logger)

    def test_checkout_validation(self):
        self.inventory_page.add_first_item_to_cart()

        self.inventory_page.go_to_cart()

        self.cart_page.proceed_to_checkout()

        self.logger.info("Testing checkout with missing information")
        self.checkout_page.continue_checkout()

        # Check for validation errors
        error_message = self.checkout_page.get_error_message()
        if error_message:
            self.checkout_page.take_screenshot("checkout_validation_error")
        else:
            self.logger.error("Expected error message not found after empty checkout submission")
            self.checkout_page.take_screenshot("checkout_validation_failed")