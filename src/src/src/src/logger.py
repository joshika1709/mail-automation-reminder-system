from datetime import datetime

def log_email(email, status):
    with open("logs/email_logs.txt", "a") as file:
        file.write(f"{datetime.now()} | {email} | {status}\n")
