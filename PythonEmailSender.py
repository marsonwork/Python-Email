import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Use the appropriate SMTP server for your email provider
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
        smtp_server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Email sending failed. Error: {str(e)}')

# Usage
if __name__ == "__main__":
    # Email configuration
    # Read the JSON configuration file
    with open('email-config.json') as config_file:
        config = json.load(config_file)

    sender_email = config['sender_email']
    sender_password = config['sender_password']
    recipient_email = 'receiver-email@gmail.com'
    subject         = 'Subject:'
    message_body    = 'Keep your message here'

    send_email(sender_email, sender_password, recipient_email, subject, message_body)
