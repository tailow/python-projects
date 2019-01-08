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


def play_move(player, column):
    for row in range(board_height):
        if board[row][column - 1] != 0:
            board[row - 1][column - 1] = player
            break

        elif row == board_height - 1:
            board[row][column - 1] = player


def analyse_move(player, column, analysis_board):
    for row in range(board_height):
        if analysis_board[row][column - 1] != 0:
            analysis_board[row - 1][column - 1] = player
            break

        elif row == board_height - 1:
            analysis_board[row][column - 1] = player

    return analysis_board


def play_game():
    while True:
        print_board()

        play_move(1, ask_player_input())

        winner = check_win(board)

        if winner:
            print_board()
            print("Player %s won!" % winner)
            return

        play_move(2, calculate_move())

        winner = check_win(board)

        if winner:
            print_board()
            print("Bot won!")
            return


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


def is_legal(move, current_board):
    if move < 1 or move > 7:
        return False

    elif current_board[0][move - 1] != 0:
        return False

    else:
        return True


def ask_player_input():
    while True:
        move = int(input("Select column: "))

        if is_legal(move, board):
            return move

        else:
            print("Illegal move!")


def calculate_move():
    analysis_board = copy.deepcopy(board)

    legal_moves = []

    for i in range(board_width + 1):
        if is_legal(i, analysis_board):
            legal_moves.append(i)

    for move in legal_moves:
        if check_win(analyse_move(2, move, analysis_board)):
            return move

    if is_legal(4, board):
        return 4

    else:
        return random.choice(legal_moves)


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
            if board_state[y][x] == board_state[y + 1][x + 1] and board_state[y][x] != 0:
                piece_count += 1

                if piece_count >= 4:
                    return board_state[y][x]

            else:
                piece_count = 1

    # Check ascending diagonal rows
    for y in range(3, board_height):
        for x in range(board_width - 3):
            if board_state[y][x] == board_state[y - 1][x + 1] and board_state[y][x] != 0:
                piece_count += 1

                if piece_count >= 4:
                    return board_state[y][x]

            else:
                piece_count = 1


board = make_board(board_width, board_height)

play_game()
