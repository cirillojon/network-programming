import smtplib, os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
load_dotenv()
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL = os.getenv('EMAIL')

try:
    # Connect to the email server
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    print("Successfully connected to the server.")
except:
    print("Error connecting to the server.")

try:
    # Login to your email
    server.login(EMAIL, EMAIL_PASS)
    print("Successfully logged in.")
except:
    print("Error logging in.")

msg = MIMEMultipart()
msg['From'] = 'Jon'
msg['To'] = 'jonathan.cirillo@ucf.edu'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
