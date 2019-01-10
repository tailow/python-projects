# CONNECT FOUR

import random
import copy

board_width = 7
board_height = 6


def make_board(width, height):

    new_list = []

    for y in range(height):
        new_list.append([])
        for x in range(width):
            new_list[y].append(0)

    return new_list


def print_board():

    print()

    for y in range(board_height):
        for x in range(board_width):

            if board[y][x] == 0:
                print("_ ", end="")

            elif board[y][x] == 1:
                print("O ", end="")

            else:
                print("X ", end="")

        print("\n")

    print("1 2 3 4 5 6 7")

    print()


def play_game():

    while True:

        print_board()

        play_move(1, ask_player_input())

        if check_win(board):
            print_board()
            print("Player won!")
            return

        if is_tied(board):
            print_board()
            print("It's a tie!")
            return

        play_move(2, calculate_move())

        if check_win(board):
            print_board()
            print("Bot won!")
            return

        if is_tied(board):
            print_board()
            print("It's a tie!")
            return


def play_move(player, column):

    # For each row, check if there is a piece
    for row in range(board_height):

        # If there is, add a piece to the row above
        if board[row][column - 1] != 0:
            board[row - 1][column - 1] = player
            break

        # If you reach the bottom of the row, add a piece there
        elif row == board_height - 1:
            board[row][column - 1] = player


def analyse_move(player, column, analysis_board):

    # For each row, check if there is a piece
    for row in range(board_height):

        # If there is, add a piece to the row above
        if analysis_board[row][column - 1] != 0:
            analysis_board[row - 1][column - 1] = player
            break

        # If you reach the bottom of the row, add a piece there
        elif row == board_height - 1:
            analysis_board[row][column - 1] = player

    return analysis_board


def ask_player_input():

    while True:
        try:
            move = int(input("Select column: "))

            if is_legal(move, board):
                return move
            else:
                print("Illegal move!")

        except ValueError:
            print("Only numbers please.")


def calculate_move():
    analysis_board = copy.deepcopy(board)

    legal_moves = []

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, analysis_board):
            legal_moves.append(i)

    # Check for winning moves
    if is_checkmate(2, analysis_board):
        return is_checkmate(2, analysis_board)

    # Check for opponent winning moves
    if is_checkmate(1, analysis_board):
        return is_checkmate(1, analysis_board)

    if is_legal(4, board):
        return 4

    else:
        return random.choice(legal_moves)


def is_legal(move, board_state):

    if move < 1 or move > 7:
        return False

    # Check if the column is full
    elif board_state[0][move - 1] != 0:
        return False

    else:
        return True


def is_checkmate(player, analysis_board):

    legal_moves = []

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, analysis_board):
            legal_moves.append(i)

    # For each move, check if there is a win
    for move in legal_moves:
        analysis_board = copy.deepcopy(board)

        # Play a move in the analysis board and check if the game is over
        if check_win(analyse_move(player, move, analysis_board)):
            return move


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


board = make_board(board_width, board_height)

play_game()
