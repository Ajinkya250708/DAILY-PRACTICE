import pickle

filename = "students.dat"

def load_data():
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except:
        return []

def save_data(students):
    with open(filename, "wb") as f:
        pickle.dump(students, f)

def add_student(students):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})
    save_data(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No records found.")
        return
    print("\nRoll\tName\t\tMarks")
    for s in students:
        print(s["roll"], "\t", s["name"], "\t\t", s["marks"])

def search_student(students):
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s["roll"] == roll:
            print("Found ->", s)
            return
    print("Student not found.")

def delete_student(students):
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")

def menu():
    print("\n===== STUDENT RECORD SYSTEM (PICKLE) =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

students = load_data()

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice, try again.")