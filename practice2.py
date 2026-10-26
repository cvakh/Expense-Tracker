expenses = [
    {"category": "food", "amount": 12.50},
    {"category": "transport", "amount": 3.00},
    {"category": "entertainment", "amount": 20.00},
]
def get_amount_from_user():
    while True:
        text = input("Amount: ")
        try:
            amount = int(text)
        except ValueError:
            print("Please enter a number.")
            continue
        if amount < 0:
            print("amounts can't be negative.")
            continue
        return amount

def print_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    print(f"{'#':<3}{"Category":<14} {"Amount":>7}")
    total = 0
    for a, i in enumerate(expenses, start=1):
        category = i["category"]
        amount = i["amount"]
        total = total + amount
        print(f"{a:<3}{category:<14}${amount:>7.2f}")
    print(f"{'':<3}{"Total":<14}${total:>7.2f}")

print_expenses(expenses)

