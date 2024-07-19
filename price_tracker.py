import os

def main():
    from_email = os.getenv('FROM_EMAIL')
    email_password = os.getenv('EMAIL_PASSWORD')
    to_email = os.getenv('TO_EMAIL')

    print(f"FROM_EMAIL: {from_email}")
    print(f"EMAIL_PASSWORD: {email_password}")
    print(f"TO_EMAIL: {to_email}")

if __name__ == "__main__":
    main()
#chnaged