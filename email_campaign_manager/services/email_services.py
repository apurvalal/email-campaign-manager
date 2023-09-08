import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, subject, html_content):
    smtp_server = "smtp.mailgun.org"
    smtp_port = 587
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    smtp_from = os.getenv("SMTP_FROM")

    headers = f"From: {smtp_from}\r\nTo: {to_email}\r\nSubject: {subject}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    email_body = headers + html_content

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_from, to_email, email_body)


def send_bulk_emails():
    # todo: add functionality
    return