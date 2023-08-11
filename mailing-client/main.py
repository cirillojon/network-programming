import smtplib, os

from dotenv import load_dotenv
load_dotenv()
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL = os.getenv('EMAIL')

print(EMAIL_PASS, EMAIL)

# Connect to the email server
server = smtplib.SMTP('smtp-mail.outlook.com', 587)
server.starttls()

# Login to your email
server.login(EMAIL, EMAIL_PASS)