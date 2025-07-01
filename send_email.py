import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = os.environ['EMAIL_USER']
password = os.environ['EMAIL_PASS']
receiver_email = "hr@example.com"  # Change to actual job email

subject = "Job Application from Gifted"
body = """
Dear HR,

Please find attached my CV and cover letter for your review.

Sincerely,
Gifted
"""

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
text = msg.as_string()
server.sendmail(sender_email, receiver_email, text)
server.quit()
