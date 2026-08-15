users = {"admin": "1234"}

def signup():
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists, try a different one.")
        return
    password = input("Choose a password: ")
    users[username] = password
    print("Account created successfully for", username)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username] == password:
        print("Welcome, ",username,"! Login successful.")
    else:
        print("Invalid username or password.")

def menu():
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        signup()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")