import os
from pages.base_page import BasePage
from locators.page_locators import InventoryPageLocators
import csv
from dotenv import load_dotenv

load_dotenv()


class InventoryPage(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.locators = InventoryPageLocators()

    def extract_product_data(self):
        self.logger.info("Extracting product data")
        products = []
        inventory_items = self.page.locator(self.locators.INVENTORY_ITEM)
        count = inventory_items.count()

        for i in range(count):
            item = inventory_items.nth(i)
            name = item.locator('.inventory_item_name').text_content()
            price = item.locator('.inventory_item_price').text_content()
            description = item.locator('.inventory_item_desc').text_content()

            products.append({
                'name': name,
                'price': price.replace('$', ''),  # Remove dollar sign for clean data
                'description': description
            })
            self.logger.info(f"Extracted product: {name} - {price}")

        return products

    def save_to_csv(self, products, filename=None):
        if filename is None:
            filename = os.getenv('CSV_OUTPUT', 'products.csv')

        self.logger.info(f"Saving product data to {filename}")

        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'price', 'description'])
            writer.writeheader()
            writer.writerows(products)

        self.logger.info(f"Successfully saved {len(products)} products to CSV")
        return filename

    def add_first_item_to_cart(self):
        self.logger.info("Adding first item to cart")
        self.click_element(self.locators.BACKPACK_ADD_BUTTON)

    def go_to_cart(self):
        self.logger.info("Navigating to cart")
        self.click_element(self.locators.SHOPPING_CART)