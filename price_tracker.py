from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

service = Service("C:/Users/Pavan/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.in/Fossil-Analog-Black-Unisex-Watch/dp/B005LBZ6G6")
