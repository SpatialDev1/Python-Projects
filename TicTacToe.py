# *ASSIGNMENT 2: Build a Tic-Tac-Toe Game in Python*
#
# *Objective:* Build a 2-player Tic-Tac-Toe game that runs in the terminal.
#
# *What Your Program Must Do:*
# - Display a 3x3 board with numbers 1-9
# - Player 1 is X, Player 2 is O
# - Players take turns choosing a position (1-9)
# - After every move, show the updated board
# - Detect a WIN (3 in a row, column, or diagonal)
# - Detect a DRAW (board full, no winner)
# - Announce the winner or draw
# - Ask "Do you want to play again? Yes/No"
#
# *Rules:*
# - If a player picks an already taken spot, show "Spot taken, try again"
# - If a player enters invalid input (e.g. a letter or 10), show an error and ask again
# - Use functions, not just one long block of code
# - Your program must run without crashing
#
# *file name: TicTacToe.py


board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def print_board(game_board):
    print()
    print("*******************************")
    print(f" {game_board[0]} | {game_board[1]} | {game_board[2]} ")
    print("-----------")
    print(f"{game_board[3]} | {game_board[4]} | {game_board[5]} ")
    print("-----------")
    print(f"{game_board[6]} | {game_board[7]} | {game_board[8]} ")
    print("*******************************")

def play(player, game_board, symbol):
    while True:
        choice = input(f"{player} choose a position between 1 and 9: ")

        if not choice.isdigit():
            print("Enter an integer!")
            continue

        position = int(choice) - 1
        if position > 8 or position < 0:
            print("Invalid number, choose a number between 1 and 9")
        elif game_board[position] == "X" or game_board[position] == "O":
            print("Sorry, that position has been taken! Choose another.")
        else:
            game_board[position] = symbol
            print_board(game_board)
            break


def check_win(game_board, is_playing):

    winning_indexes = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6],
    ]
    for row in winning_indexes:
        if game_board[row[0]] == game_board[row[1]] == game_board[row[2]] == "X":
            return is_playing == False, "Player 1", False
        elif game_board[row[0]] == game_board[row[1]] == game_board[row[2]] == "O":
            return is_playing == False, "Player 2", False

    full_board = True
    for pos in game_board:
        if pos in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            full_board = False
            break
    if full_board:
        return False, None, True

    # if game_board[0] == game_board[1] == game_board[2] == "X":
    return is_playing == True, None, False
    #     print("Player 1 won")
    # elif game_board[0] == game_board[4] == game_board[8] == "X":
    #     print("Player 1 won")
    # elif game_board[0] == game_board[3] == game_board[6] == "X":
    #     print("Player 1 won")








def main():
    global board
    is_running = True
    while is_running:
        board = board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        is_playing = True
        draw = False
        while is_playing and not draw:
            print_board(board)
            play("player1", board, "X")
            is_playing, winner, draw = check_win(board, is_playing)
            if not is_playing or draw:
                print_board(board)
                if winner:
                    print(f"The winner is {winner}🏆")
                elif draw:
                    print("It is a draw")
                break


            play("player2", board, "O")
            is_playing, winner, draw = check_win(board, is_playing)
            if not is_playing or draw:
                print_board(board)
                if winner:
                    print(f"The winner is {winner}🏆")
                elif draw:
                    print("It is a draw")
                break
        while True:
            again = input("Do you want to play again: ").strip().lower()
            if again.startswith("y"):
                break
            else:
                print("Thanks for playing")
                is_running = False
                break

if __name__ == "__main__":
    main()





