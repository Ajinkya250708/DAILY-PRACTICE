import random
import time
import pickle

file = "players.dat"
bal = 10000


def load():
    try:
        f = open(file, "rb")      # "rb" = read binary
        players = pickle.load(f)
        f.close()
        return players
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        return {}


def save(players):
    f = open(file, "wb")
    pickle.dump(players, f)
    f.close()


def register(players):
    print("\n----- CREATE NEW ACCOUNT -----")
    user_name = input("CHOOSE A USERNAME: ").strip()

    if user_name in players:
        print("THAT USERNAME ALREADY EXISTS. TRY LOGGING IN INSTEAD.")
        return None

    password = input("CHOOSE A PASSWORD: ").strip()

    players[user_name] = {
        "password": password,
        "balance": bal
    }
    save(players)
    print("\nACCOUNT CREATED! WELCOME ", user_name.upper(), ", YOU START WITH ", bal, ".")
    return user_name


def login(players):
    print("\n----- LOGIN -----")
    user_name = input("USERNAME: ").strip()
    password = input("PASSWORD: ").strip()

    if user_name in players and players[user_name]["password"] == password:
        print("\nWELCOME BACK, ", user_name.upper(), "!")
        return user_name
    else:
        print("INCORRECT USERNAME OR PASSWORD.")
        return None


def remove_player(players):
    print("\n----- REMOVE PLAYER -----")
    user_name = input("USERNAME TO REMOVE: ").strip()
    password = input("PASSWORD (CONFIRM): ").strip()

    if user_name in players and players[user_name]["password"] == password:
        confirm = input("ARE YOU SURE YOU WANT TO DELETE " + user_name + "? : ")
        if confirm.upper() == "Y" or confirm.upper() == "YES":
            del players[user_name]
            save(players)
            print("PLAYER REMOVED.")
        else:
            print("CANCELLED.")
    else:
        print("INCORRECT USERNAME OR PASSWORD. CANNOT REMOVE.")


def show_leaderboard(players):
    print("\n----------------- LEADERBOARD -----------------")
    if not players:
        print("NO PLAYERS YET.")
    else:
        ranked = sorted(players.items(), key=lambda p: p[1]["balance"], reverse=True)
        for rank, (name, info) in enumerate(ranked, start=1):
            print(str(rank) + ". " + name.ljust(15) + " BALANCE: " + str(info["balance"]))
    print("-------------------------------------------------\n")


def wait():
    n = 5
    while n > 0:
        print("SPINNING......")
        time.sleep(1)
        n -= 1
    print("THE RESULT IS:")


def pool():
    num = random.randint(1, 32)
    col = random.choice(["RED", "BLACK"])
    print(num, col)
    return num, col


def play_casino(players, user_name):

    ans = "Y"

    while ans.upper() == "Y" or ans.upper() == "YES":

        current_bal = players[user_name]["balance"]

        if current_bal <= 0:
            print("YOU ARE OUT OF BALANCE. GAME OVER.")
            break

        print("\nCURRENT BALANCE: " + str(current_bal))
        print("OPTIONS:")
        print("1.NUMBER")
        print("2.COLOUR")
        print("\n")

        user = input("CHOOSE YOUR BET ON: ")
        current = int(input("HOW MUCH WOULD YOU LIKE TO BET: "))

        if current > current_bal:
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
                        current_bal -= current
                        current = current * 2
                        current_bal += current
                        print("YOU WON! New Balance:", current_bal)
                    else:
                        current_bal -= current
                        print("YOU LOST! New Balance:", current_bal)
                elif user2.upper() == "BLACK" or user2 == "2":
                    if col == "BLACK":
                        current_bal -= current
                        current = current * 2
                        current_bal += current
                        print("YOU WON! New Balance:", current_bal)
                    else:
                        current_bal -= current
                        print("YOU LOST! New Balance:", current_bal)
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
                        current_bal -= current
                        current = current * 32
                        current_bal += current
                        print("YOU WON! New Balance:", current_bal)
                    else:
                        current_bal -= current
                        print("YOU LOST! New Balance:", current_bal)

                elif uff == "2":
                    print("GROUPS: 1)1-2 2)3-4 3)5-6 ..... 16)31-32")
                    II = int(input("PICK GROUP NUMBER(1-16):"))
                    wait()
                    num, col = pool()
                    groups = {
                        1: [1, 2], 2: [3, 4], 3: [5, 6], 4: [7, 8],
                        5: [9, 10], 6: [11, 12], 7: [13, 14], 8: [15, 16],
                        9: [17, 18], 10: [19, 20], 11: [21, 22], 12: [23, 24],
                        13: [25, 26], 14: [27, 28], 15: [29, 30], 16: [31, 32]
                    }
                    if num in groups[II]:
                        current_bal -= current
                        current *= 16
                        current_bal += current
                        print("YOU WON! New Balance:", current_bal)
                    else:
                        current_bal -= current
                        print("YOU LOST! New Balance:", current_bal)

                elif uff == "3":
                    print("GROUPS: 1)1-4 2)5-8 3)9-12 ..... 8)29-32")
                    III = int(input("PICK GROUP NUMBER(1-8):"))
                    wait()
                    num, col = pool()
                    groups = {
                        1: [1, 2, 3, 4], 2: [5, 6, 7, 8],
                        3: [9, 10, 11, 12], 4: [13, 14, 15, 16],
                        5: [17, 18, 19, 20], 6: [21, 22, 23, 24],
                        7: [25, 26, 27, 28], 8: [29, 30, 31, 32]
                    }
                    if num in groups[III]:
                        current_bal -= current
                        current *= 8
                        current_bal += current
                        print("YOU WON! New Balance:", current_bal)
                    else:
                        current_bal -= current
                        print("YOU LOST! New Balance:", current_bal)

                elif uff == "4":
                    print("GROUPS: 1)1-8 2)9-16 3)17-24 4)25-32")
                    IV = int(input("PICK GROUP NUMBER(1-4):"))
                    wait()
                    num, col = pool()
                    groups = {
                        1: [1, 2, 3, 4, 5, 6, 7, 8],
                        2: [9, 10, 11, 12, 13, 14, 15, 16],
                        3: [17, 18, 19, 20, 21, 22, 23, 24],
                        4: [25, 26, 27, 28, 29, 30, 31, 32]
                    }
                    if num in groups[IV]:
                        current_bal -= current
                        current *= 4
                        current_bal += current
                        print("YOU WON! New Balance:", current_bal)
                    else:
                        current_bal -= current
                        print("YOU LOST! New Balance:", current_bal)

                elif uff == "5":
                    print("GROUPS: 1)1-16 2)17-32")
                    V = int(input("PICK GROUP NUMBER(1 OR 2):"))
                    wait()
                    num, col = pool()
                    groups = {
                        1: list(range(1, 17)),
                        2: list(range(17, 33))
                    }
                    if num in groups[V]:
                        current_bal -= current
                        current *= 2
                        current_bal += current
                        print("YOU WON! New Balance:", current_bal)
                    else:
                        current_bal -= current
                        print("YOU LOST! New Balance:", current_bal)

                else:
                    print("Invalid choice")

            else:
                print("Invalid bet type")

        players[user_name]["balance"] = current_bal
        save(players)

        print("\nCurrent Balance:", players[user_name]["balance"])

        if players[user_name]["balance"] <= 0:
            print("YOU ARE OUT OF BALANCE. GAME OVER.")
            break

        ans = input("\nDO YOU WANT TO PLACE ANOTHER BET, OR (E)XIT TO MENU? : ")
        if ans.upper() == "E" or ans.upper() == "EXIT":
            break

    print("\nTHANKS FOR PLAYING, ", user_name.upper(), "! FINAL BALANCE:", players[user_name]["balance"])


def main():
    players = load()   # loaded once from the binary file at startup

    print("\n")
    print("-----------------------------------CASINO-----------------------------------\n")
    print("WELCOME TO OUR CASINO\n")

    while True:
        print("\n================ MAIN MENU ================")
        print("1. LOGIN")
        print("2. REGISTER (NEW PLAYER)")
        print("3. LEADERBOARD")
        print("4. REMOVE A PLAYER")
        print("5. EXIT")
        print("=============================================")

        choice = input("CHOOSE AN OPTION: ").strip()

        if choice == "1":
            user_name = login(players)
            if user_name:
                play_casino(players, user_name)

        elif choice == "2":
            register(players)

        elif choice == "3":
            show_leaderboard(players)

        elif choice == "4":
            remove_player(players)

        elif choice == "5":
            print("\nGOODBYE! THANKS FOR VISITING THE CASINO.")
            break

        else:
            print("INVALID OPTION. TRY AGAIN.")


if __name__ == "__main__":
    main()