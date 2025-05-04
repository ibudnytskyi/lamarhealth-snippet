from playwright.sync_api import Page
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


class BasePage:
    def __init__(self, page: Page, logger):
        self.page = page
        self.logger = logger
        self.base_url = "https://www.saucedemo.com"

    def navigate_to(self, path=""):
        url = f"{self.base_url}/{path}"
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def click_element(self, selector):
        self.logger.info(f"Clicking element: {selector}")
        self.page.locator(selector).click()

    def fill_field(self, selector, value):
        self.logger.info(f"Filling field {selector} with value: {value}")
        self.page.locator(selector).fill(value)

    def get_text(self, selector):
        return self.page.locator(selector).text_content()

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def take_screenshot(self, name):
        screenshot_dir = os.getenv('SCREENSHOT_DIR', 'automation_screenshots')

        # Ensure directory exists
        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{screenshot_dir}/{name}_{timestamp}.png"
        self.page.screenshot(path=filename)
        self.logger.info(f"Screenshot saved: {filename}")
        return filename