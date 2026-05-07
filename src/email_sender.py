import smtplib
import os
from email.message import EmailMessage

def send_email(to_email, subject, body, dry_run=False):

    if dry_run:
        print(f"[DRY RUN] Email to {to_email}")
        return "DRY_RUN"

    EMAIL = os.getenv("EMAIL_USER")
    PASSWORD = os.getenv("EMAIL_PASS")

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

    return "SUCCESS"
