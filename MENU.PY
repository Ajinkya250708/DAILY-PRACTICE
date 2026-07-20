print("WELCOME TO OUR RESTAURANT")
print("----------MENU-----------\n")

cost = 0

def menu():
    print("1. PIZZA (₹350)")
    print("2. PASTA (₹250)")
    print("3. BROWNIE (₹110)")
    print("4. WAFFLE (₹150)")

def selc():
    global cost
    selection = input("WHAT WOULD YOU LIKE TO HAVE: ")
    if selection == "1":
        cost += 350
    elif selection == "2":
        cost += 250
    elif selection == "3":
        cost += 110
    elif selection == "4":
        cost += 150
    else:
        print("Invalid selection, please try again.\t")

menu()
selc()

more = input("DO YOU WANT ANYTHING ELSE (Y/N): ")
while more.upper() == "Y":
    selc()
    more = input("DO YOU WANT ANYTHING ELSE (Y/N): ")

print("\t")
print("YOUR TOTAL IS:", "₹", cost, "YOUR ORDER WILL BE READY IN 10 MINUTES")
print("THANK YOU!!")
