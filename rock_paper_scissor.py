import random

print("WELCOME TO ROCK PAPER SCISSORS")

L = ["rock", "paper", "scissors"]

ans = "Y"

while ans.upper() == "Y":
    user = input("Enter Rock, Paper, or Scissors: ").lower()
    computer = random.choice(L)
    
    print("Computer chose:", computer)
    
    if user == computer:
        print("It's a tie!")
    elif user == "rock" and computer == "scissors":
        print("You win!")
    elif user == "paper" and computer == "rock":
        print("You win!")
    elif user == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")
    
    ans = input("Play again? (Y/N): ")

print("Thanks for playing!")