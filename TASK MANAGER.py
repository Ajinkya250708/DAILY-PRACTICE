tasks = []

def add_task():
    task = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ")
    tasks.append({"task": task, "priority": priority, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\n----- YOUR TASKS -----")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. [{t['priority']}] {t['task']} - {status}")

def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark done: "))
    tasks[num-1]["done"] = True
    print("Marked as done!")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    tasks.pop(num-1)
    print("Task deleted!")

def menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Bye! Good luck with your tasks!")
        break
    else:
        print("Invalid choice")