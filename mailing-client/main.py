import smtplib, os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from dotenv import load_dotenv

load_dotenv()
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL = os.getenv('EMAIL')
EMAIL_TO = os.getenv('EMAIL_TO')

try:
    # Connect to the email server
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    print("Successfully connected to the server.")
except smtplib.SMTPException:
    print("Error connecting to the server.")
    raise

try:
    # Login to your email
    server.login(EMAIL, EMAIL_PASS)
    print("Successfully logged in.")
except smtplib.SMTPException:
    print("Error logging in.")
    raise

msg = MIMEMultipart()
msg['From'] = EMAIL
msg['To'] = EMAIL_TO
msg['Subject'] = 'Just a Test'

try:
    with open('message.txt', 'r') as f:
        message = f.read()
    msg.attach(MIMEText(message, 'plain'))
except FileNotFoundError:
    print("Error opening message.txt. File might not exist.")
    raise

try:
    filename = 'image.jpeg'
    with open(filename, 'rb') as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(p)
except FileNotFoundError:
    print(f"Error opening {filename}. File might not exist.")
    raise

try:
    text = msg.as_string()
    server.sendmail(EMAIL, EMAIL_TO, text)
    print("Email sent successfully!")
except smtplib.SMTPException:
    print("Error sending the email.")
    raise

server.quit()
