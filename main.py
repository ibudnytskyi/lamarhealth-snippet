import logging
import os
from playwright.sync_api import sync_playwright
from tests.test_login import LoginTest
from tests.test_product import ProductTest
from tests.test_checkout import CheckoutTest
from dotenv import load_dotenv

load_dotenv()

# Set up logging
def setup_logging():
    screenshot_dir = os.getenv('SCREENSHOT_DIR', 'automation_screenshots')
    log_file = os.getenv('LOG_FILE', 'automation.log')

    os.makedirs(screenshot_dir, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


def main():
    logger = setup_logging()
    logger.info("Starting automation script for saucedemo.com")

    headless = os.getenv('HEADLESS', 'True').lower() == 'true'
    browser_type = os.getenv('BROWSER', 'chromium')
    slowmo = int(os.getenv('SLOWMO', '0'))
    timeout = int(os.getenv('TIMEOUT', '30000'))

    with sync_playwright() as p:
        browser_instance = getattr(p, browser_type)
        browser = browser_instance.launch(
            headless=headless,
            slow_mo=slowmo
        )

        context = browser.new_context(viewport={'width': 1280, 'height': 720})
        context.set_default_timeout(timeout)
        page = context.new_page()

        try:
            logger.info("Navigating to saucedemo.com")
            page.goto('https://www.saucedemo.com')

            login_test = LoginTest(page, logger)
            login_test.run_tests()

            product_test = ProductTest(page, logger)
            products = product_test.extract_and_save_products()

            checkout_test = CheckoutTest(page, logger)
            checkout_test.test_checkout_validation()

            logger.info("Automation completed successfully")

        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            screenshot_dir = os.getenv('SCREENSHOT_DIR', 'automation_screenshots')
            screenshot_path = f"{screenshot_dir}/error_state.png"
            page.screenshot(path=screenshot_path)
            logger.info(f"Error screenshot saved: {screenshot_path}")
        finally:
            browser.close()


if __name__ == "__main__":
    main()