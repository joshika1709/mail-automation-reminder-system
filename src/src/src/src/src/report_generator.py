import pandas as pd

def save_report(data):
    df = pd.DataFrame(data, columns=["email", "status", "time"])
    df.to_csv("outputs/report.csv", index=False)
