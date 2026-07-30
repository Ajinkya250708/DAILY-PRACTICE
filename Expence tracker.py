import csv

filename = "expenses.csv"

def add_expense():
    file = open(filename, "a", newline="")
    w = csv.writer(file)
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")
    w.writerow([date, category, amount, desc])
    file.close()
    print("Expense added successfully!")

def view_expenses():
    file = open(filename, "r")
    r = csv.reader(file)
    print("\nDate\t\tCategory\tAmount\tDescription")
    for i in r:
        print(i[0], "\t", i[1], "\t\t", i[2], "\t", i[3])
    file.close()

def category_total():
    category = input("Enter category to check total: ")
    file = open(filename, "r")
    r = csv.reader(file)
    total = 0
    found = False
    for i in r:
        if i[1].lower() == category.lower():
            total += float(i[2])
            found = True
    file.close()
    if found:
        print(f"Total spent on {category}: ₹{total}")
    else:
        print("No expenses found in this category.")

def total_expense():
    file = open(filename, "r")
    r = csv.reader(file)
    total = 0
    for i in r:
        total += float(i[2])
    file.close()
    print(f"Total expense so far: ₹{total}")

def delete_expense():
    desc = input("Enter description of expense to delete: ")
    file = open(filename, "r")
    r = csv.reader(file)
    rows = list(r)
    file.close()

    new_rows = []
    deleted = False
    for i in rows:
        if i[3] == desc:
            deleted = True
        else:
            new_rows.append(i)

    file = open(filename, "w", newline="")
    w = csv.writer(file)
    w.writerows(new_rows)
    file.close()

    if deleted:
        print("Expense deleted successfully!")
    else:
        print("Expense not found.")

def menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category-wise Total")
    print("4. Total Expense")
    print("5. Delete Expense")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_total()
    elif choice == "4":
        total_expense()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice, try again.")