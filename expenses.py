import csv
import os
from datetime import date

FILENAME = "expenses.csv"
FIELDS = ["date", "amount", "category", "description"]

def add_expense(amount, category, description):
    file_exists = os.path.exists(FILENAME)  #check if the file exists
    with open(FILENAME, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "date": date.today().isoformat(),
            "amount": amount,
            "category": category,
            "description": description,
        })

def load_expenses():
    if not os.path.exists(FILENAME):
        return []
    expenses = []
    with open(FILENAME, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)
    return expenses

print(load_expenses())