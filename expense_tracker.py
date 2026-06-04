import csv
import os

FILE_NAME = "expenses.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Description", "Amount"])


def add_expense():
    desc = input("Enter expense description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            next(reader)

            print("\nExpenses:")
            for row in reader:
                print(f"{row[0]} - ₹{row[1]}")

    except FileNotFoundError:
        print("No expenses found.")


def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            total += float(row[1])

    print(f"\nTotal Expenses: ₹{total}")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")