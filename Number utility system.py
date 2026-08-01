def fact():
    n = int(input("Enter the number: "))
    p = 1
    while n >= 1:
        p *= n
        n = n - 1
    print("Factorial is:", p)

def table():
    n = int(input("Enter the number: "))
    print("Table of", n, ":")
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

def even_odd():
    n = int(input("Enter the number: "))
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

def prime():
    n = int(input("Enter the number: "))
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
    if is_prime:
        print(n, "is Prime")
    else:
        print(n, "is Not Prime")

def sum_digits():
    n = int(input("Enter the number: "))
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    print("Sum of digits is:", total)

def reverse_number():
    n = int(input("Enter the number: "))
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    print("Reverse of", original, "is:", reverse)

def palindrome():
    n = int(input("Enter the number: "))
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        print(original, "is a Palindrome")
    else:
        print(original, "is Not a Palindrome")

def armstrong():
    n = int(input("Enter the number: "))
    original = n
    total = 0
    num_digits = len(str(n))
    while n > 0:
        digit = n % 10
        total += digit ** num_digits
        n = n // 10
    if total == original:
        print(original, "is an Armstrong number")
    else:
        print(original, "is Not an Armstrong number")

def fibonacci():
    n = int(input("Enter how many terms: "))
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def menu():
    print("\n===== NUMBER UTILITY PROGRAM =====")
    print("1. Factorial")
    print("2. Multiplication Table")
    print("3. Even or Odd")
    print("4. Prime Check")
    print("5. Sum of Digits")
    print("6. Reverse Number")
    print("7. Palindrome Check")
    print("8. Armstrong Number Check")
    print("9. Fibonacci Series")
    print("10. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        fact()
    elif choice == "2":
        table()
    elif choice == "3":
        even_odd()
    elif choice == "4":
        prime()
    elif choice == "5":
        sum_digits()
    elif choice == "6":
        reverse_number()
    elif choice == "7":
        palindrome()
    elif choice == "8":
        armstrong()
    elif choice == "9":
        fibonacci()
    elif choice == "10":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice, try again.")