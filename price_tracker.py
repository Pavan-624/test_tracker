from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Define path for GeckoDriver on Linux
geckodriver_path = '/usr/local/bin/geckodriver'

# Set up Firefox options
options = Options()
options.add_argument('--headless')  # Run Firefox in headless mode (no GUI)
options.add_argument('--no-sandbox')  # Disable sandboxing to avoid security restrictions in CI environments

# Set up Firefox service
service = Service(executable_path=geckodriver_path)

# Initialize Firefox WebDriver
try:
    driver = webdriver.Firefox(service=service, options=options)
    driver.get('https://www.amazon.in/Fossil-Analog-Black-Unisex-Watch/dp/B005LBZ6G6')
    print("Page title is:", driver.title)
finally:
    driver.quit()
