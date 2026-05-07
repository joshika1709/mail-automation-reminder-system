# 📧 Email Automation & Reminder System

---

## 🚀 Project Overview

The **Email Automation & Reminder System** is a Python-based application designed to automate sending emails and reminders using structured data, scheduling, and SMTP.

This project simulates how organizations automate repetitive communication tasks such as interview reminders, payment follow-ups, and event notifications.

---

## ❗ Problem Statement

In many organizations:

* Emails are sent manually
* Reminders are often missed
* Communication is inconsistent
* No proper tracking exists

👉 This leads to:

* Wasted time
* Human errors
* Poor productivity

---

## 🏢 Industry Relevance

This system is widely applicable across industries:

### 👩‍💼 HR Teams

* Interview reminders
* Candidate follow-ups

### 📈 Sales Teams

* Lead nurturing
* Demo reminders

### 🏫 Training & Education

* Webinar alerts
* Assignment reminders

### 🧾 Operations

* Payment reminders
* Task notifications

👉 Helps organizations:

* Save time
* Reduce manual work
* Improve communication efficiency

---

## ✨ Features

* 📂 Read contacts from CSV
* ⏰ Schedule email reminders
* 📧 Send emails using SMTP
* 🧩 Dynamic email templates
* 🔄 Personalized messages
* 📝 Logging system (success/failure tracking)
* 📊 CSV report generation
* 🧪 Dry-run mode for safe testing

---

## 🛠️ Tech Stack

* **Python**
* **pandas** (data handling)
* **smtplib** (email sending)
* **email.message** (email formatting)
* **schedule** (task scheduling)
* **datetime** (time handling)
* **logging** (tracking system activity)
* **CSV files** (data storage)

---

## 📁 Folder Structure

```
Email-Automation-Reminder-System/
│
├── data/              # Input CSV files
├── templates/         # Email templates
├── src/               # Core Python modules
├── outputs/           # Generated reports
├── logs/              # Log files
├── images/            # Screenshots
├── docs/              # Documentation
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---


### 🧪 Dry Run Mode (Safe Testing)

In `main.py`:

```python
DRY_RUN = True
```

Run:

```bash
python main.py
```

---

### 📧 Real Email Mode

```python
DRY_RUN = False
```

Run:

```bash
python main.py
```

---

## 📊 Sample Output

### Terminal Output

```
Scheduler started...
[DRY RUN] Email to rahul.test@gmail.com | Subject: Interview Reminder
```

---

### Log File (`logs/email_logs.txt`)

```
2026-05-06 15:30 | rahul.test@gmail.com | DRY_RUN
```

---

### Report File (`outputs/report.csv`)

```
email,status,time
rahul.test@gmail.com,DRY_RUN,15:30
```

---

## 🧠 Learning Outcomes

Through this project, you will learn:

* Python automation fundamentals
* Working with CSV and structured data
* Email automation using SMTP
* Task scheduling in Python
* Logging and monitoring systems
* Writing modular and scalable code
* GitHub project structuring
* Real-world workflow simulation

---

## 🎯 Conclusion

This project demonstrates how Python can be used to automate repetitive communication workflows, making it highly relevant for roles in:

* Python Development
* Automation Engineering
* HR Operations
* Business Analytics
* Admin & Operations

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it on LinkedIn!

---
