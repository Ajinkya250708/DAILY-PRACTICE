import random

def toss():
    print("---------- TOSS --------------")
    ANS = "Y"
    
    while ANS.upper() == "Y":
        n = random.randint(1, 2)
        if n==1:
            result="Heads"
        else:
            result="Tails"
        print(f"You tossed: {result}")
        play_again = input("Toss again? (Y/N): ")
    
    print("Thanks for playing!")

toss()