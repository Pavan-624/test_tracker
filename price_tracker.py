import json
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Load configuration from environment variable
config = json.loads(os.getenv('ENV_DATA'))

# Setup Firefox options
options = Options()
options.add_argument('--headless')  # Run in headless mode

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
