from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Define path for GeckoDriver on Linux
geckodriver_path = '/usr/local/bin/geckodriver'

# Set up Firefox options
options = Options()
# options.add_argument('--headless')  # Comment out or remove this line

# Set up Firefox service
service = Service(executable_path=geckodriver_path)

# Initialize Firefox WebDriver
driver = webdriver.Firefox(service=service, options=options)
