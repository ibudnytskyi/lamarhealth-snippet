# Lamarhealth Automation Snippet

Automation project for [Lamarhealth](https://www.saucedemo.com) website using Playwright with Python and the Page Object Model design pattern.

# Features

- Login testing (valid/invalid credentials)
- Product data extraction to CSV
- Checkout validation testing
- Error handling with screenshots
- Detailed logging

# Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Install dependencies: `pip install -r requirements.txt`
5. Install Playwright browsers: `playwright install`
6. Configure environment: `cp .env.example .env`

# Usage

Run the tests:
```
python main.py
```

# Project Structure

- `main.py` - Main entry point
- `pages/` - Page object classes
- `tests/` - Test implementations
- `locators/` - Element selectors
- `data/` - Test data
- `generator/` - Test data generation

# Reflection Questions

# What steps did you prioritize first? Why?
I prioritized setting up the Page Object Model architecture first to create a maintainable foundation, separating element locators from test logic for better organization and future scalability.

# What was critical to complete in the 1 hour?
The critical components were the basic framework architecture, login functionality, product data extraction, checkout validation, and error handling with screenshots.

# How long did you actually spend on the project?
Approximately 2 hours - one hour for core implementation, plus additional time for enhancements, environment variables, error handling.

# How did you know your automation was working?
By observing console output, checking logs, verifying CSV data extraction, examining screenshots, and ensuring all test steps completed successfully.

# What would you improve with more time?
With more time, I would add test parallelization, expanded test coverage, better reporting, CI/CD integration, and cross-browser testing capabilities.
