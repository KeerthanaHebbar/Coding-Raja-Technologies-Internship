import json
import os

# File to store budget data
DATA_FILE = "budget_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {
            "income": 0,
            "expenses": [],
            "categories": {}
        }


def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def display_menu():
    print("\nBudget Tracker Menu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget Summary")
    print("4. Exit")


def add_income(data):
    amount = float(input("Enter income amount: $"))
    data["income"] += amount
    print(f"Income of ${amount} added successfully.")


def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input(f"Enter expense amount for {category}: $"))
    data["expenses"].append({"category": category, "amount": amount})
    data["categories"].setdefault(category, 0)
    data["categories"][category] += amount
    print(f"Expense of ${amount} added successfully.")


def view_budget_summary(data):
    print("\nBudget Summary:")
    print(f"Total Income: ${data['income']:.2f}")

    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    print(f"Total Expenses: ${total_expenses:.2f}")

    print("Expense Breakdown:")
    for category, amount in data['categories'].items():
        print(f"{category}: ${amount:.2f}")

    remaining_budget = data['income'] - total_expenses
    print(f"Remaining Budget: ${remaining_budget:.2f}")


def main():
    data = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            view_budget_summary(data)
        elif choice == '4':
            save_data(data)
            print("Exiting Budget Tracker. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
