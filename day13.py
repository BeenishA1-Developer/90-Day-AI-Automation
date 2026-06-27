# day13.py — Expense Tracker
import json

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    category = input("Category (food/transport/shopping): ")
    amount = float(input("Amount (PKR): "))
    expenses.append({"category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense added!")

def show_summary(expenses):
    if not expenses:
        print("No expenses yet!")
        return
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Spent: PKR {total}")
    for e in expenses:
        print(f"  {e['category']}: PKR {e['amount']}")
    print("-" * 25)  # Yeh ek line draw kar dega farq dekhne ke liye!

def main():
    expenses = load_expenses()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            break

main()