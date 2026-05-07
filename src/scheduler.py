import schedule
import time
from datetime import datetime
from src.email_sender import send_email
from src.logger import log_email
from src.report_generator import save_report

def schedule_jobs(contacts, reminders, template, dry_run=False):

    report_data = []

    for _, reminder in reminders.iterrows():

        send_time = reminder['send_time']

        def job(rem=reminder):

            print(f"Running job at {datetime.now()}")

            for _, contact in contacts.iterrows():

                message = template.replace("{name}", contact['name'])
                message = message.replace("{message}", rem['message'])

                status = send_email(
                    contact['email'],
                    rem['subject'],
                    message,
                    dry_run
                )

                log_email(contact['email'], status)

                report_data.append([
                    contact['email'],
                    status,
                    datetime.now().strftime("%H:%M")
                ])

            save_report(report_data)

        schedule.every().day.at(send_time).do(job)

    print("Scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)
