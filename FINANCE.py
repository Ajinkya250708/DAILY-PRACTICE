def simple_interest():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest (%): "))
    t = float(input("Enter Time (years): "))
    si = (p * r * t) / 100
    total = p + si
    print(f"\nSimple Interest: ₹{si:.2f}")
    print(f"Total Amount: ₹{total:.2f}")

def compound_interest():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest (%): "))
    t = float(input("Enter Time (years): "))
    n = int(input("Enter compounding frequency per year (e.g. 1, 4, 12): "))
    amount = p * (1 + (r / (n * 100))) ** (n * t)
    ci = amount - p
    print(f"\nCompound Interest: ₹{ci:.2f}")
    print(f"Total Amount: ₹{amount:.2f}")

def emi_calculator():
    p = float(input("Enter Loan Amount: "))
    annual_rate = float(input("Enter Annual Interest Rate (%): "))
    years = float(input("Enter Loan Tenure (years): "))
    
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    
    if monthly_rate == 0:
        emi = p / months
    else:
        emi = (p * monthly_rate * (1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    
    total_payment = emi * months
    total_interest = total_payment - p
    
    print(f"\nMonthly EMI: ₹{emi:.2f}")
    print(f"Total Payment: ₹{total_payment:.2f}")
    print(f"Total Interest: ₹{total_interest:.2f}")

def tip_calculator():
    bill = float(input("Enter Bill Amount: "))
    tip_percent = float(input("Enter Tip Percentage: "))
    people = int(input("Enter number of people splitting: "))
    
    tip_amount = (bill * tip_percent) / 100
    total = bill + tip_amount
    per_person = total / people
    
    print(f"\nTip Amount: ₹{tip_amount:.2f}")
    print(f"Total Bill: ₹{total:.2f}")
    print(f"Amount per person: ₹{per_person:.2f}")

def discount_calculator():
    price = float(input("Enter Original Price: "))
    discount_percent = float(input("Enter Discount Percentage: "))
    
    discount_amount = (price * discount_percent) / 100
    final_price = price - discount_amount
    
    print(f"\nDiscount Amount: ₹{discount_amount:.2f}")
    print(f"Final Price: ₹{final_price:.2f}")

def menu():
    print("\n===== FINANCE CALCULATOR TOOLKIT =====")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. EMI Calculator")
    print("4. Tip Calculator")
    print("5. Discount Calculator")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        simple_interest()
    elif choice == "2":
        compound_interest()
    elif choice == "3":
        emi_calculator()
    elif choice == "4":
        tip_calculator()
    elif choice == "5":
        discount_calculator()
    elif choice == "6":
        print("Thank you for using Finance Toolkit!")
        break
    else:
        print("Invalid choice, try again.")