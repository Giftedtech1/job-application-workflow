
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email setup
sender_email = os.environ['EMAIL_USER']
password = os.environ['EMAIL_PASS']
receiver_email = "hr@example.com"  # Replace with target job email

# Email content
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Job Application from Gifted"

body = "Dear HR,\n\nPlease find my resume attached for your review.\n\nRegards,\nGifted"
msg.attach(MIMEText(body, 'plain'))

# Attach resume
filename = "resume.pdf"
with open(filename, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {filename}')
    msg.attach(part)

# Send email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully.")
