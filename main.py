from expenses import add_expense, load_expenses

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
    print("3. Quit")

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()