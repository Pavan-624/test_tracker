from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json

# Load environment variables
env_data = os.getenv('ENV_DATA')

# Optionally load other environment variables if needed
if env_data:
    env_vars = json.loads(env_data)
    print("Loaded environment variables")

# Define path for GeckoDriver on GitHub Actions (Linux path)
geckodriver_path = '/snap/bin/geckodriver'

# Set up Firefox options
options = Options()
options.add_argument('--headless')  # Uncomment if you need headless mode

# Set up Firefox service
service = Service(executable_path=geckodriver_path)

# Initialize Firefox WebDriver
driver = None  # Initialize driver to None

try:
    driver = webdriver.Firefox(service=service, options=options)
    
    # Open the URL
    driver.get('https://www.amazon.in/s?k=iphone+15+pro+max')
    
    # Wait for an element with the class "a-size-medium a-color-base a-text-normal" to appear
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.a-size-medium.a-color-base.a-text-normal'))
        )
        print("Product element detected")
    except Exception as e:
        print(f"Product element not detected: {e}")
    
    print(driver.title)  # Print the page title to verify it loads correctly

finally:
    if driver:
        driver.quit()
