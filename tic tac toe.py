game_board = [" "] * 9

def show_board():
    print(f"\n {game_board[0]} | {game_board[1]} | {game_board[2]} ")
    print("---+---+---")
    print(f" {game_board[3]} | {game_board[4]} | {game_board[5]} ")
    print("---+---+---")
    print(f" {game_board[6]} | {game_board[7]} | {game_board[8]} \n")


def find_winner():
    winning_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   
        [0, 4, 8], [2, 4, 6]               
    ]

    for pattern in winning_patterns:
        first, second, third = pattern
        if game_board[first] == game_board[second] == game_board[third] != " ":
            return game_board[first]

    return None


def board_is_full():
    return " " not in game_board


def start_game():
    player_turn = "X"

    while True:
        show_board()
        print(f"It's Player {player_turn}'s turn")

        user_choice = input("Choose a position (1-9): ")

        if not user_choice.isdigit() or int(user_choice) not in range(1, 10):
            print("Please enter a valid number between 1 and 9.")
            continue

        chosen_spot = int(user_choice) - 1

        if game_board[chosen_spot] != " ":
            print("That spot is already taken. Try another one.")
            continue

        game_board[chosen_spot] = player_turn

        game_result = find_winner()

        if game_result:
            show_board()
            print(f"🎉 Congratulations! Player {game_result} wins!")
            break

        if board_is_full():
            show_board()
            print("The game ends in a draw!")
            break

        if player_turn == "X":
            player_turn = "O"
        else:
            player_turn = "X"


print("=" * 35)
print("     WELCOME TO TIC-TAC-TOE")
print("=" * 35)

start_game()