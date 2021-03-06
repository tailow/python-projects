# CONNECT FOUR

import connectfourbot

board_width = 7
board_height = 6

played_moves = []


def make_board(width, height):
    board = []

    for y in range(height):
        board.append([])
        for x in range(width):
            board[y].append(0)

    return board


def print_board(board, previous_move):
    for y in range(board_height):
        for x in range(board_width):
            if board[y][x] == 0:
                print("_", end=" ")

            elif board[y][x] == 1:
                print("X", end=" ")

            else:
                print("O", end=" ")

        print()

    print("1 2 3 4 5 6 7")

    for column in range(board_width):
        if column == previous_move - 1:
            print("^", end=" ")
        else:
            print(" ", end=" ")

    print()


def play_game():
    board = make_board(board_width, board_height)

    previous_move = -1

    while True:
        print("\nBoard evaluation: " + str(connectfourbot.evaluate_board(board)))

        # Player 1 play move
        print_board(board, previous_move)

        move = ask_for_input(board)

        play_move(1, move, board)
        previous_move = move

        played_moves.append(move)

        if check_win(board):
            print_board(board, previous_move)
            print("Player won!\n")
            return

        if is_tied(board):
            print_board(board, previous_move)
            print("It's a tie!\n")
            return

        print("\nBoard evaluation: " + str(connectfourbot.evaluate_board(board)))

        # Player 2 play move
        print_board(board, previous_move)

        move = connectfourbot.calculate_move(board, 2)

        play_move(2, move, board)
        previous_move = move

        played_moves.append(move)

        if check_win(board):
            print_board(board, previous_move)
            print("Bot won!\n")
            return

        if is_tied(board):
            print_board(board, previous_move)
            print("It's a tie!\n")
            return


def play_move(player, column, board):
    # For each row, check if there is a piece
    for row in range(board_height):
        # If there is, add a piece to the row above
        if board[row][column - 1] != 0:
            board[row - 1][column - 1] = player
            break

        # If you reach the bottom of the row, add a piece there
        elif row == board_height - 1:
            board[row][column - 1] = player


def ask_for_input(board):
    while True:
        try:
            player_input = int(input("Select column: "))

        except ValueError:
            print("Invalid input.")
            continue

        if is_legal(player_input, board):
            return player_input

        else:
            print("Illegal move!")


def is_legal(move, board_state):
    if move < 1 or move > 7:
        return False

    # Check if the column is full
    elif board_state[0][move - 1] != 0:
        return False

    else:
        return True


def is_tied(board_state):
    legal_moves = []

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, board_state):
            legal_moves.append(i)

    if len(legal_moves) == 0:
        return True

    else:
        return False


def check_win(board_state):
    piece_count = 1

    # Check horizontal rows
    for y in range(board_height):
        for x in range(board_width - 1):
            if board_state[y][x] == board_state[y][x + 1] and board_state[y][x] != 0:
                piece_count += 1

                if piece_count >= 4:
                    return board_state[y][x]

            else:
                piece_count = 1

        piece_count = 1

    # Check vertical rows
    for x in range(board_width):
        for y in range(board_height - 1):
            if board_state[y][x] == board_state[y + 1][x] and board_state[y][x] != 0:
                piece_count += 1

                if piece_count >= 4:
                    return board_state[y][x]

            else:
                piece_count = 1

        piece_count = 1

    # Check descending diagonal rows
    for y in range(board_height - 3):
        for x in range(board_width - 3):
            if board_state[y][x] == board_state[y + 1][x + 1] == board_state[y + 2][x + 2] == board_state[y + 3][x + 3]\
                    and board_state[y][x] != 0:

                return board_state[y][x]

    # Check ascending diagonal rows
    for y in range(3, board_height):
        for x in range(board_width - 3):
            if board_state[y][x] == board_state[y - 1][x + 1] == board_state[y - 2][x + 2] == board_state[y - 3][x + 3]\
                    and board_state[y][x] != 0:

                return board_state[y][x]


while True:
    choice = input("Would you like to play a game? (Y/N)")

    if choice.upper() == "Y":
        play_game()

    elif choice.upper() == "N":
        break

    else:
        print("Invalid input.\n")
