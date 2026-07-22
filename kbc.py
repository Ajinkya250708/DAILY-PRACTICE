print("--------------------------KBC---------------------------------\n")
print("Rules:\n")
print("1. Each question has 4 options; only one is correct.")
print("2. Amount will be added automatically.")
print("3. Wrong answer ends the game.")
print("4. One lifeline allowed per game.")
print("5. Type Q anytime to quit and keep your winnings.\n")

amount = 0

print("QUESTION 1:\n")
print("INTERNATIONAL LITERACY DAY IS CELEBRATED ON")
print("A) 8 SEP")
print("B) 22 JULY")
print("C) 27 JUNE")
print("D) 14 AUGUST")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "A":
    amount = 1000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 2:\n")
print("WHO IS KNOWN AS THE FATHER OF THE NATION IN INDIA?")
print("A) NEHRU")
print("B) GANDHI")
print("C) PATEL")
print("D) BOSE")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "B":
    amount = 2000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 3:\n")
print("WHAT IS THE CAPITAL OF INDIA?")
print("A) MUMBAI")
print("B) KOLKATA")
print("C) NEW DELHI")
print("D) CHENNAI")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "C":
    amount = 5000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 4:\n")
print("WHICH IS THE LARGEST PLANET IN THE SOLAR SYSTEM?")
print("A) EARTH")
print("B) JUPITER")
print("C) MARS")
print("D) SATURN")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "B":
    amount = 10000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 5:\n")
print("WHO WROTE THE INDIAN NATIONAL ANTHEM?")
print("A) TAGORE")
print("B) PREMCHAND")
print("C) IQBAL")
print("D) NAIDU")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "A":
    amount = 25000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 6:\n")
print("WHAT IS THE NATIONAL SPORT OF INDIA?")
print("A) CRICKET")
print("B) HOCKEY")
print("C) FOOTBALL")
print("D) KABADDI")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "B":
    amount = 50000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 7:\n")
print("WHICH RIVER IS KNOWN AS THE GANGA OF THE SOUTH?")
print("A) KAVERI")
print("B) GODAVARI")
print("C) KRISHNA")
print("D) NARMADA")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "B":
    amount = 100000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 8:\n")
print("WHICH IS THE LONGEST RIVER IN THE WORLD?")
print("A) AMAZON")
print("B) NILE")
print("C) GANGA")
print("D) YANGTZE")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "B":
    amount = 500000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 9:\n")
print("WHO PAINTED THE MONA LISA?")
print("A) PICASSO")
print("B) VAN GOGH")
print("C) LEONARDO DA VINCI")
print("D) MICHELANGELO")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "C":
    amount = 2500000
    print("CORRECT ANSWER")
    print(f"Total winnings: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()


print("\nQUESTION 10 (FINAL):\n")
print("WHICH IS THE LARGEST OCEAN IN THE WORLD?")
print("A) ATLANTIC OCEAN")
print("B) INDIAN OCEAN")
print("C) ARCTIC OCEAN")
print("D) PACIFIC OCEAN")

a = input("CHOOSE OPTION: ").upper()

if a == "Q":
    print(f"You quit. Total winnings: Rs {amount}")
    exit()

if a == "D":
    amount = 10000000
    print("CORRECT ANSWER")
    print(f"CONGRATULATIONS! You won the jackpot: Rs {amount}")
else:
    print(f"WRONG ANSWER. Game over. Total winnings: Rs {amount}")
    exit()