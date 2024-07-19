from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Path to GeckoDriver
geckodriver_path = r'C:\Users\Pavan\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe'

# Setup Firefox options
options = Options()
# Add any necessary options here, e.g., headless mode
# options.add_argument('--headless')

# Setup GeckoDriver service
service = Service(executable_path=geckodriver_path)

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Use the driver for your automation tasks
driver.get("https://www.amazon.in/s?k=iphone+15")

# Your email sending code here

driver.quit()
