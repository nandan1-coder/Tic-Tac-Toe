#Name:Nandan Kumar Ray
#ERP:RU-26-02777
#E-mail:nandan.kumar@rungta.org
#section:B2
#Project title: Tic Tac Toe Game
def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board, player):
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in winning_lines:
        if board[line[0]] == player and \
           board[line[1]] == player and \
           board[line[2]] == player:
            return line

    return None


def play_game():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    player = "X"
    moves = 0

    while moves < 9:
        display_board(board)

        try:
            position = int(input("Player " + player + ", enter position (1-9): "))
        except ValueError:
            print("Invalid position. Enter a number from 1 to 9.")
            continue

        if position < 1 or position > 9:
            print("Invalid position. Enter a number from 1 to 9.")
            continue

        index = position - 1

        if board[index] == "X" or board[index] == "O":
            print("Position already taken. Choose another position.")
            continue

        board[index] = player
        moves += 1

        winning_line = check_winner(board, player)

        if winning_line:
            display_board(board)
            print("Player " + player + " wins!")
            print("Winning line:", end=" ")

            for i in winning_line:
                print(i + 1, end=" ")

            print()
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    display_board(board)
    print("Board is full after 9 moves. It's a draw! No moves left.")


while True:
    play_game()

    again = input("Play again? (y/n): ")

    if again.lower() != "y":
        print("Thank you for playing!")
        break