from faker import Faker
import random
from datetime import datetime, timedelta


class DataGenerator:
    def __init__(self, locale='en_US', seed=None):
        """Initialize the data generator with optional locale and seed"""
        self.faker = Faker(locale)
        if seed:
            Faker.seed(seed)  # Set a seed for reproducible results

    def generate_person(self):
        """Generate complete person data including name, address, contact info"""
        return {
            'first_name': self.faker.first_name(),
            'last_name': self.faker.last_name(),
            'email': self.faker.email(),
            'phone': self.faker.phone_number(),
            'address': self.generate_address(),
            'birth_date': self.faker.date_of_birth(minimum_age=18, maximum_age=80),
            'ssn': self.faker.ssn(),
            'job': self.faker.job()
        }

    def generate_address(self):
        """Generate a complete address"""
        return {
            'street': self.faker.street_address(),
            'city': self.faker.city(),
            'state': self.faker.state(),
            'zip': self.faker.zipcode(),
            'country': self.faker.country()
        }

    def generate_credit_card(self):
        """Generate credit card information"""
        return {
            'number': self.faker.credit_card_number(),
            'expiry': self.faker.credit_card_expire(),
            'provider': self.faker.credit_card_provider(),
            'security_code': self.faker.credit_card_security_code()
        }

    def generate_date(self, start_date=None, end_date=None):
        """Generate a random date between start_date and end_date"""
        if not start_date:
            start_date = datetime.now() - timedelta(days=365)
        if not end_date:
            end_date = datetime.now()

        return self.faker.date_between(start_date=start_date, end_date=end_date)

    def generate_test_user(self):
        """Generate test user data specifically for testing applications"""
        return {
            'username': self.faker.user_name(),
            'password': self.faker.password(length=12, special_chars=True, digits=True,
                                            upper_case=True, lower_case=True),
            'email': self.faker.email(),
            'registration_date': self.faker.date_time_this_year()
        }

    def generate_company_data(self):
        """Generate company information"""
        return {
            'name': self.faker.company(),
            'slogan': self.faker.catch_phrase(),
            'industry': self.faker.industry(),
            'employee_count': random.randint(5, 10000),
            'founded_date': self.faker.date_this_century(before_today=True),
            'website': self.faker.url()
        }

    def generate_product_data(self, category=None):
        """Generate product information"""
        categories = ['Electronics', 'Clothing', 'Home Goods', 'Food', 'Books']
        if not category:
            category = random.choice(categories)

        return {
            'name': self.faker.word().capitalize() + ' ' + self.faker.word().capitalize(),
            'description': self.faker.paragraph(),
            'price': round(random.uniform(1.0, 999.99), 2),
            'category': category,
            'sku': self.faker.bothify(text='???-########'),
            'in_stock': random.choice([True, False])
        }