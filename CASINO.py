import random
import time

def wait():
    n = 5
    while n > 0:
        print("SPINNING")
        time.sleep(1)
        n -= 1
    print("THE RESULT IS:")

def pool():
    num = random.randint(1, 32)
    col = random.choice(["RED", "BLACK"])
    print(num, col)
    return num, col

print("\n")
print("-----------------------------------CASINO-----------------------------------\n")
print("WELCOME TO OUR CASINO\n")

bal = int(input("HOW MUCH MONEY WOULD YOU LIKE TO DEPOSITE: "))
print("\n")

ans = "Y"

while ans.upper() =="Y" or ans.upper()=="YES" :

    if bal <= 0:
        print("YOU ARE OUT OF BALANCE. GAME OVER.")
        break

    print("OPTIONS")
    print("1.NUMBER")
    print("2.COLOUR")
    print("\n")

    user = input("CHOOSE YOUR BET ON: ")
    current = int(input("HOW MUCH WOULD YOU LIKE TO BET: "))

    if current > bal:
        print("NOT ENOUGH BALANCE")

    else:

        if user == "2" or user.upper() == "COLOUR":
            print("\n")
            print("OPTIONS:\n")
            print("1.RED")
            print("2.BLACK")

            user2 = input("CHOOSE COLOUR: ")
            wait()
            num, col = pool()

            if user2.upper() == "RED" or user2 == "1":
                if col == "RED":
                    bal -= current
                    current = current * 2
                    bal += current
                    print("YOU WON! New Balance:", bal)
                else:
                    bal -= current
                    print("YOU LOST! New Balance:", bal)
            elif user2.upper() == "BLACK" or user2 == "2":
                if col == "BLACK":
                    bal -= current
                    current = current * 2
                    bal += current
                    print("YOU WON! New Balance:", bal)
                else:
                    bal -= current
                    print("YOU LOST! New Balance:", bal)
            else:
                print("Invalid colour choice")

        elif user == "1" or user.upper() == "NUMBER":
            print("OPTIONS:")
            print("1. Single Number        (32x payout)")
            print("2. Group of 2 Numbers   (16x payout)")
            print("3. Group of 4 Numbers   (8x payout)")
            print("4. Group of 8 Numbers   (4x payout)")
            print("5. Group of 16 Numbers  (2x payout)\n")

            uff = input("Enter your choice: ")

            if uff == "1":
                I = int(input("Pick a number (1-32):"))
                wait()
                num, col = pool()
                if num == I:
                    bal -= current
                    current = current * 32
                    bal += current
                    print("YOU WON! New Balance:", bal)
                else:
                    bal -= current
                    print("YOU LOST! New Balance:", bal)

            elif uff == "2":
                print("GROUPS: 1)1-2 2)3-4 3)5-6 ..... 16)31-32")
                II = int(input("PICK GROUP NUMBER(1-16):"))
                wait()
                num, col = pool()
                groups = {
                    1: [1,2], 2: [3,4], 3: [5,6], 4: [7,8],
                    5: [9,10], 6: [11,12], 7: [13,14], 8: [15,16],
                    9: [17,18], 10: [19,20], 11: [21,22], 12: [23,24],
                    13: [25,26], 14: [27,28], 15: [29,30], 16: [31,32]
                }
                if num in groups[II]:
                    bal -= current
                    current *= 16
                    bal += current
                    print("YOU WON! New Balance:", bal)
                else:
                    bal -= current
                    print("YOU LOST! New Balance:", bal)

            elif uff == "3":
                print("GROUPS: 1)1-4 2)5-8 3)9-12 ..... 8)29-32")
                III = int(input("PICK GROUP NUMBER(1-8):"))
                wait()
                num, col = pool()
                groups = {
                    1: [1,2,3,4], 2: [5,6,7,8],
                    3: [9,10,11,12], 4: [13,14,15,16],
                    5: [17,18,19,20], 6: [21,22,23,24],
                    7: [25,26,27,28], 8: [29,30,31,32]
                }
                if num in groups[III]:
                    bal -= current
                    current *= 8
                    bal += current
                    print("YOU WON! New Balance:", bal)
                else:
                    bal -= current
                    print("YOU LOST! New Balance:", bal)

            elif uff == "4":
                print("GROUPS: 1)1-8 2)9-16 3)17-24 4)25-32")
                IV = int(input("PICK GROUP NUMBER(1-4):"))
                wait()
                num, col = pool()
                groups = {
                    1: [1,2,3,4,5,6,7,8],
                    2: [9,10,11,12,13,14,15,16],
                    3: [17,18,19,20,21,22,23,24],
                    4: [25,26,27,28,29,30,31,32]
                }
                if num in groups[IV]:
                    bal -= current
                    current *= 4
                    bal += current
                    print("YOU WON! New Balance:", bal)
                else:
                    bal -= current
                    print("YOU LOST! New Balance:", bal)

            elif uff == "5":
                print("GROUPS: 1)1-16 2)17-32")
                V = int(input("PICK GROUP NUMBER(1 OR 2):"))
                wait()
                num, col = pool()
                groups = {
                    1: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
                    2: [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
                }
                if num in groups[V]:
                    bal -= current
                    current *= 2
                    bal += current
                    print("YOU WON! New Balance:", bal)
                else:
                    bal -= current
                    print("YOU LOST! New Balance:", bal)

            else:
                print("Invalid choice")

        else:
            print("Invalid bet type")

    print("\nCurrent Balance:", bal)
    ans = input("\nDO YOU WANT TO PLACE ANOTHER BET? : ")

print("\nTHANKS FOR PLAYING! FINAL BALANCE:", bal)