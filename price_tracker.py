import os
import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Load configuration from environment variable
env_data = os.getenv('ENV_DATA')
if env_data is None:
    raise ValueError("ENV_DATA environment variable is not set or is empty.")

config = json.loads(env_data)

# Setup Firefox options
options = Options()
# Add any necessary options here, e.g., headless mode
# options.add_argument('--headless')

# Setup GeckoDriver service
service = Service(executable_path='/usr/local/bin/geckodriver')  # Path for Linux

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Use the driver for your automation tasks
driver.get("https://www.amazon.in/s?k=iphone+15")

# Example of using email settings from config
from_email = config["FROM_EMAIL"]
to_email = config["TO_EMAIL"]
email_password = config["EMAIL_PASSWORD"]

# Your email sending code here

driver.quit()
