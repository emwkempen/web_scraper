import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 465  # For SSL
smtp_server = 'smtp.gmail.com'
sender_email = 'nc894fienjcvqieopwv@gmail.com'
password = '+zYS2gz/]e^L=UD@'
receiver_email = 'emwkempen@gmail.com'\
    # , 'sietskevliet@gmail.com'

message = MIMEMultipart('alternative')
message['From'] = 'Emiel'
message['To'] = receiver_email


def send_email(subject, text, html):
    message['Subject'] = subject

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

