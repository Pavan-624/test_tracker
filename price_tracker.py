import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Hardcoded credentials
FROM_EMAIL = "pavanthatikonda2235@gmail.com"
EMAIL_PASSWORD = "nyvu pohv vqdn tzdx"
TO_EMAIL = "thatikondapavan26@gmail.com"

# ChromeDriver path
CHROMEDRIVER_PATH = r"C:\Users\Pavan\Downloads\chromedriver-win64 (1)\chromedriver-win64"

# Amazon product URL
PRODUCT_URL = "https://www.amazon.in/Fossil-Analog-Black-Unisex-Watch/dp/B005LBZ6G6"

# Price threshold
PRICE_THRESHOLD = 15000

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(FROM_EMAIL, EMAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(FROM_EMAIL, TO_EMAIL, text)
            print(f"Email sent to {TO_EMAIL}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(PRODUCT_URL)
        time.sleep(5)  # Wait for the page to load
        
        price_element = driver.find_element(By.ID, 'priceblock_ourprice')  # Update selector as needed
        price_text = price_element.text
        price = float(price_text.replace(',', '').replace('₹', '').strip())
        
        print(f"Product Price: {price}")
        
        if price <= PRICE_THRESHOLD:
            subject = f"Price Drop Alert: {PRODUCT_URL}"
            body = f"The price of the product at {PRODUCT_URL} has dropped to ₹{price}. Act now!"
            send_email(subject, body)
        else:
            print("Price is above the threshold.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
