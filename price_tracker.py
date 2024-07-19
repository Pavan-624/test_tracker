import json
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Load configuration from environment variable
env_data = os.getenv('ENV_DATA')
if env_data is None:
    raise ValueError("ENV_DATA environment variable is not set")
config = json.loads(env_data)

# Setup Firefox options
options = Options()
options.add_argument('--headless')  # Run in headless mode

# Setup GeckoDriver service
geckodriver_path = '/usr/local/bin/geckodriver'  # Path for Linux
service = Service(executable_path=geckodriver_path)

# Debugging information
print(f"Using GeckoDriver at: {geckodriver_path}")
print(f"Firefox options: {options.arguments}")

# Initialize the Firefox WebDriver
try:
    driver = webdriver.Firefox(service=service, options=options)
    print("Successfully initialized Firefox WebDriver")
except Exception as e:
    raise RuntimeError(f"Failed to initialize Firefox WebDriver: {e}")

# Example of your automation task
try:
    driver.get("https://www.amazon.in/s?k=iphone+15")
    print("Successfully navigated to the URL")
except Exception as e:
    print(f"Failed to navigate to the URL: {e}")

# Example of using email settings from config
from_email = config["FROM_EMAIL"]
to_email = config["TO_EMAIL"]
email_password = config["EMAIL_PASSWORD"]

# Your email sending code here

# Quit the driver
try:
    driver.quit()
    print("Successfully quit the driver")
except Exception as e:
    print(f"Failed to quit the driver: {e}")
