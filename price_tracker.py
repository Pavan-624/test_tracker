import os
import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Load environment variables
env_data = os.getenv('ENV_DATA')

# Optionally load other environment variables if needed
if env_data:
    env_vars = json.loads(env_data)
    print("Loaded environment variables")

# Fetch secrets from environment variables
from_email = env_vars['FROM_EMAIL']
from_password = env_vars['EMAIL_PASSWORD']
to_email = env_vars['TO_EMAIL']

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# URL and threshold for a single product
product = {
    "url": "https://www.amazon.in/Fossil-Analog-Black-Unisex-Watch/dp/B005LBZ6G6",
    "threshold": 141489.0
}

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, from_password)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")

def fetch_data():
    driver = None
    try:
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Run in headless mode

        # Define path for GeckoDriver on GitHub Actions (Linux path)
        geckodriver_path = '/snap/bin/geckodriver'
        service = Service(geckodriver_path)

        # Initialize the Firefox WebDriver
        driver = webdriver.Firefox(service=service, options=firefox_options)
        
        delay_time = 10  # Fixed delay time in seconds

        # Open the URL
        driver.get(product["url"])
        time.sleep(delay_time)  # Use fixed delay time

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Adjust these selectors based on actual HTML structure
        name_tag = soup.find('span', class_='a-size-large product-title-word-break')
        name = name_tag.text.strip() if name_tag else 'N/A'
        print(f"Product Name: {name}")

        price_tag = soup.find('span', class_='a-price-whole')
        price = price_tag.text.strip().replace(',', '') if price_tag else 'N/A'
        print(f"Product Price: {price}")

        if price != 'N/A':
            price = float(price)
            print(f"Fetched Price: {price}")

            # Always send an email if the price is below the threshold
            if price <= product["threshold"]:
                print(f'Price is below threshold for {name}: {price}')
                send_email(
                    'Price Drop Alert!',
                    f'The price of {name} has dropped to {price}.',
                    to_email
                )
        else:
            print("Price data not available.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    fetch_data()
