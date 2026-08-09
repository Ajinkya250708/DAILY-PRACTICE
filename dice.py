import random

def dice():
    print("---------- DICE ROLL --------------")
    ANS = "Y"
    
    while ANS.upper() == "Y":
        n = random.randint(1, 6)
        print(f"You rolled: {n}")
        play_again = input("Toss again? (Y/N): ")
    
    print("Thanks for playing!")

dice()