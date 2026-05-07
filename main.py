from src.data_loader import load_contacts, load_reminders
from src.template_loader import load_template
from src.scheduler import schedule_jobs

DRY_RUN = True

contacts = load_contacts("data/contacts.csv")
reminders = load_reminders("data/reminders.csv")
template = load_template("templates/email_template.txt")

schedule_jobs(contacts, reminders, template, dry_run=DRY_RUN)
