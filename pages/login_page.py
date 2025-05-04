from pages.base_page import BasePage
from locators.page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.locators = LoginPageLocators()

    def login(self, username, password):
        self.logger.info(f"Attempting login with username: {username}")
        self.fill_field(self.locators.USERNAME_INPUT, username)
        self.fill_field(self.locators.PASSWORD_INPUT, password)
        self.click_element(self.locators.LOGIN_BUTTON)
        self.logger.info("Login form submitted")

    def get_error_message(self):
        if self.is_visible(self.locators.ERROR_MESSAGE):
            error_msg = self.get_text(self.locators.ERROR_MESSAGE)
            self.logger.warning(f"Login validation error: {error_msg}")
            return error_msg
        return None

    def clear_form(self):
        self.fill_field(self.locators.USERNAME_INPUT, "")
        self.fill_field(self.locators.PASSWORD_INPUT, "")