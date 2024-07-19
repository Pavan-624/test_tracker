import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os
import ast

# Load environment variables from ENV_DATA secret
config = ast.literal_eval(os.getenv('ENV_DATA'))

# Setup Firefox options
options = Options()
# Add any necessary options here, e.g., headless mode
# options.add_argument('--headless')

# Setup GeckoDriver service
service = Service(executable_path='/usr/local/bin/geckodriver')

# Initialize the Firefox WebDriver
try:
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://www.amazon.in/s?k=iphone+15")

    # Example of using email settings from config
    from_email = config["FROM_EMAIL"]
    to_email = config["TO_EMAIL"]
    email_password = config["EMAIL_PASSWORD"]

    # Your email sending code here

finally:
    driver.quit()
