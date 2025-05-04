from pages.inventory_page import InventoryPage


class ProductTest:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.inventory_page = InventoryPage(page, logger)

    def extract_and_save_products(self):
        products = self.inventory_page.extract_product_data()

        self.validate_product_data(products)

        self.inventory_page.save_to_csv(products)

        return products

    def validate_product_data(self, products):
        self.logger.info(f"Validating extracted product data ({len(products)} products)")

        if len(products) == 0:
            self.logger.error("No products found on the page")
            self.inventory_page.take_screenshot("no_products_found")
            return

        # Basic validation on each product
        for i, product in enumerate(products):
            if not product['name'] or not product['price']:
                self.logger.error(f"Product at index {i} has missing required data")
                self.inventory_page.take_screenshot("invalid_product_data")