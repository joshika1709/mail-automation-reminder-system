import pandas as pd

def load_contacts(path):
    return pd.read_csv(path)

def load_reminders(path):
    return pd.read_csv(path)
