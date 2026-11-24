from expenses import add_expense, load_expenses, monthly_total, total_by_category, get_int

def get_amount_from_user():
    while True:
        text = input("Amount: ")
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a number.")
            continue
        if amount <= 0:
            print("amounts need to be greater than 0.")
            continue
        return amount

def print_expense(expenses):
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

def show_menu():
    print()
    print("=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Monthly total")
    print("4. Total by category")
    print("5. Quit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            amount = get_amount_from_user()
            category = input("Category: ").strip().lower()
            description = input("Description: ").strip()
            add_expense(amount, category, description)
            print("Expense saved!")
        elif choice == "2":
            print_expense(load_expenses())
        elif choice == "3":
            year = get_int("Year (e.g. 2026): ", 2000, 2100)
            month = get_int("Month (1-12): ", 1, 12)
            total = monthly_total(load_expenses(), year, month)
            print(f"Total for {year}-{month:02d}: ${total:.2f}")
        elif choice == "4":
            totals = total_by_category(load_expenses())
            if not totals:
                print("No expenses yet.")
            for category, total in totals.items():
                print(f"{category:<14}${total:>8.2f}")
        elif choice == "5":
            print("alr see you ^^")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()