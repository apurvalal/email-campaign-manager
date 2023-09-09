import smtplib
import os
import logging
from threading import Thread
from dotenv import load_dotenv

logger = logging.getLogger('django')
load_dotenv()

def send_email(to_email, subject, html_content):
    try:
        smtp_server = "smtp.mailgun.org"
        smtp_port = 587
        smtp_username = os.getenv("SMTP_USERNAME")
        smtp_password = os.getenv("SMTP_PASSWORD")
        smtp_from = os.getenv("SMTP_FROM")

        headers = f"From: {smtp_from}\r\nTo: {to_email}\r\nSubject: {subject}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
        email_body = headers + html_content
        
        logger.info(f"Sending email to {to_email} with subject: {subject}")

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_from, to_email, email_body)

    except Exception as e:
        logger.error(f"An error occurred while sending the email: {str(e)}")


def send_bulk_emails(email_list, subject, html_content):
    threads = []
    try:
        logger.info(f"Sending bulk emails with subject: {subject}")

        # Multi-threaded sending of emails
        for email in email_list:
            thread = Thread(target=send_email, args=(email, subject, html_content))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    except Exception as e:
        logger.error(f"An error occurred while sending bulk emails: {str(e)}")
