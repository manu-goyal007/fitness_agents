# agent_b/utils.py
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"  # Example: Gmail
SMTP_PORT = 587
SMTP_USER = "goyalm685@gmail.com"
SMTP_PASSWORD = "wnkt xufw btyj inzh"

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, [to_email], msg.as_string())

