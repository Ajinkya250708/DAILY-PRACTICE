import csv

filename = "student.csv"

def add():
    file = open(filename, "a", newline="")
    w = csv.writer(file)
    n = int(input("Enter number of entries: "))
    for i in range(n):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        w.writerow([roll, name, marks])
    file.close()
    print("Records added successfully!")

def dis():
    file = open(filename, "r")
    r = csv.reader(file)
    print("R.No\tName\t\tMarks")
    for i in r:
        print(i[0], "\t", i[1], "\t\t", i[2])
    file.close()

def search():
    roll = input("Enter Roll Number to search: ")
    file = open(filename, "r")
    r = csv.reader(file)
    found = False
    for i in r:
        if i[0] == roll:
            print("Found -> R.No:", i[0], "Name:", i[1], "Marks:", i[2])
            found = True
            break
    file.close()
    if not found:
        print("Record not found.")

def delete():
    roll = input("Enter Roll Number to delete: ")
    file = open(filename, "r")
    r = csv.reader(file)
    rows = list(r)
    file.close()

    new_rows = []
    deleted = False
    for i in rows:
        if i[0] == roll:
            deleted = True
        else:
            new_rows.append(i)

    file = open(filename, "w", newline="")
    w = csv.writer(file)
    w.writerows(new_rows)
    file.close()

    if deleted:
        print("Record deleted successfully!")
    else:
        print("Record not found.")

def menu():
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        dis()
    elif choice == "3":
        search()
    elif choice == "4":
        delete()
    elif choice == "5":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice, try again.")