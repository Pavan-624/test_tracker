import os
import json

# Get the secret data from the environment variable
env_data = os.getenv('ENV_DATA')

if env_data:
    # Parse the JSON string
    secrets = json.loads(env_data)

    # Extract individual values
    from_email = secrets.get('FROM_EMAIL')
    email_password = secrets.get('EMAIL_PASSWORD')
    to_email = secrets.get('TO_EMAIL')

    # Use these values as needed
    print(f"From Email: {from_email}")
    print(f"To Email: {to_email}")

else:
    print("No environment data found.")
