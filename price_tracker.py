import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get the secret data from the environment variable
env_data = os.getenv('ENV_DATA')

if env_data:
    # Parse the JSON string
    secrets = json.loads(env_data)

    # Extract individual values
    from_email = secrets.get('FROM_EMAIL')
    email_password = secrets.get('EMAIL_PASSWORD')
    to_email = secrets.get('TO_EMAIL')

    # Use these values to send an email
    print(f"From Email: {from_email}")
    print(f"To Email: {to_email}")

    # Email content
    subject = "Test Email from GitHub Actions"
    body = "This is a test email sent from a GitHub Actions workflow."

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(from_email, email_password)
        
        # Send the email
        text = message.as_string()
        server.sendmail(from_email, to_email, text)
        print("Email sent successfully")
        
        # Disconnect from the server
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
else:
    print("No environment data found.")
