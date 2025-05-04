import os
from dotenv import load_dotenv
import sys

load_dotenv()

required_env_vars = [
    'VALID_USER', 'VALID_PASS',
    'INVALID_USER', 'INVALID_PASS',
    'TEST_FIRST_NAME', 'TEST_LAST_NAME', 'TEST_POSTAL_CODE'
]

missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    print("Please set these variables in your .env file")
    sys.exit(1)


class TestData:
    VALID_USER = os.getenv('VALID_USER')
    VALID_PASS = os.getenv('VALID_PASS')
    INVALID_USER = os.getenv('INVALID_USER')
    INVALID_PASS = os.getenv('INVALID_PASS')

    FIRST_NAME = os.getenv('TEST_FIRST_NAME')
    LAST_NAME = os.getenv('TEST_LAST_NAME')
    POSTAL_CODE = os.getenv('TEST_POSTAL_CODE')