# Go over to our gmail account and setup 2 factor authentication
# Generate app password
# Create a function to send mail

# tqbxopobvskuzyow

from email.message import EmailMessage
from decouple import config
 
# if you get ImportError: cannot import name 'config' from 'decouple'
# pip uninstall decouple
# pip install python-decouple
# this should correct the ImportError

import ssl
import smtplib

API_EMAIL_PASSWORD = config('password_EmailSenderApp')

email_sender = 'jeffrey.l.asuncion@gmail.com'
# next step create environment variable instead
email_password = API_EMAIL_PASSWORD

email_receiver = 'bluedragonmatawan@gmail.com'

subject = "Don't forget to subscribe."

body = """
When you watch a video, please hit subscribe
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Email sent!")