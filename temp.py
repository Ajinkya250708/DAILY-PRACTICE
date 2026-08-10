def convert():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")
    elif choice == "3":
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273.15
        print(f"{c}°C = {k:.2f}K")
    elif choice == "4":
        k = float(input("Enter temperature in Kelvin: "))
        c = k - 273.15
        print(f"{k}K = {c:.2f}°C")
    elif choice == "5":
        f = float(input("Enter temperature in Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print(f"{f}°F = {k:.2f}K")
    elif choice == "6":
        k = float(input("Enter temperature in Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print(f"{k}K = {f:.2f}°F")
    else:
        print("Invalid choice")

convert()