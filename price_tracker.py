import os
from selenium import webdriver

# Access environment variables
from_email = os.getenv('FROM_EMAIL')
email_password = os.getenv('EMAIL_PASSWORD')
to_email = os.getenv('TO_EMAIL')

# Ensure these variables are being used correctly in your script
print(f"From Email: {from_email}")
print(f"To Email: {to_email}")

# Your existing script logic here
