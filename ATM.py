balance = 10000
pin = "2507"

def check_balance():
    print("Your balance is: ₹", balance)

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Invalid amount")
    else:
        balance += amount
        print("Deposit successful! New balance: ₹", balance)

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawal successful! New balance: ₹", balance)

def menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

attempts = 3
verified = False

while attempts > 0:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        verified = True
        break
    else:
        attempts -= 1
        print(f"Wrong PIN. {attempts} attempts left.")

if verified:
    print("Login successful!")
    while True:
        menu()
        choice = input("Select an option: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid option, try again.")
else:
    print("Too many wrong attempts. Card blocked.")