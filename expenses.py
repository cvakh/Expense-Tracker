import csv
import os
from datetime import date, datetime

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

def monthly_total(expenses, year, month):
    total = 0
    for e in expenses:
        d = datetime.strptime(e["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            total += e["amount"]
    return total

def total_by_category(expense):
    totals = {}
    for k in expense:
        category = k['category']
        totals[category] = totals.get(category, 0) + k['amount']
    return totals

if __name__ == "__main__":
    fake = [
        {"date": "2026-11-05", "amount": 10.0, "category": "food"},
        {"date": "2026-11-20", "amount": 5.0, "category": "fun"},
        {"date": "2026-10-30", "amount": 99.0, "category": "food"},
    ]
print(monthly_total(fake, 2026, 11))
print(total_by_category(fake))