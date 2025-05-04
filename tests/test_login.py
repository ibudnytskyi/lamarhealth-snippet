from pages.login_page import LoginPage
from data.data import TestData


class LoginTest:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.login_page = LoginPage(page, logger)
        self.test_data = TestData()

    def run_tests(self):
        self.test_invalid_login()

        self.login_page.clear_form()

        self.test_valid_login()

    def test_invalid_login(self):
        self.logger.info("Testing invalid login credentials")
        self.login_page.login(
            self.test_data.INVALID_USER,
            self.test_data.INVALID_PASS
        )

        error_message = self.login_page.get_error_message()
        if error_message:
            self.login_page.take_screenshot("invalid_login_error")
        else:
            self.logger.error("Expected error message not found after invalid login")

    def test_valid_login(self):
        self.logger.info("Testing valid login credentials")
        self.login_page.login(
            self.test_data.VALID_USER,
            self.test_data.VALID_PASS
        )

        current_url = self.page.url
        if "inventory.html" in current_url:
            self.logger.info("Login successful")
        else:
            self.logger.error(f"Login failed. Current URL: {current_url}")
            self.login_page.take_screenshot("login_failed")