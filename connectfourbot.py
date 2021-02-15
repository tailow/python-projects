# CONNECT 4 BOT

import copy
import math

board_height = 6
board_width = 7

search_depth = 4
lines_of_three_multiplier = 4
lines_of_two_multiplier = 2
middle_multiplier = 5


def calculate_move(board, player):
    best_move = 0

    if player == 1:
        best_evaluation = -math.inf

        for move in legal_moves(board):
            evaluation = minimax(analyse_move(1, move, board), search_depth, False, math.inf, -math.inf)

            if evaluation >= best_evaluation:
                best_evaluation = evaluation
                best_move = move

    else:
        best_evaluation = math.inf

        for move in legal_moves(board):
            evaluation = minimax(analyse_move(2, move, board), search_depth, True, -math.inf, math.inf)

            if evaluation <= best_evaluation:
                best_evaluation = evaluation
                best_move = move

    print()

    return best_move


def minimax(board, depth, is_maximizing_player, alpha, beta):
    if depth <= 0:
        return evaluate_board(board)

    if is_maximizing_player:
        evaluation = -math.inf

        for move in legal_moves(board):
            evaluation = max(evaluation, minimax(analyse_move(1, move, board), depth - 1, False, alpha, beta))
            alpha = max(alpha, evaluation)

            if alpha >= beta:
                break

        return evaluation

    else:
        evaluation = math.inf

        for move in legal_moves(board):
            evaluation = min(evaluation, minimax(analyse_move(2, move, board), depth - 1, True, alpha, beta))
            beta = min(beta, evaluation)

            if beta <= alpha:
                break

        return evaluation


def evaluate_board(board):
    evaluation = 0

    p1_lines_of_two, p1_lines_of_three = pieces_per_line(1, board)
    p2_lines_of_two, p2_lines_of_three = pieces_per_line(2, board)

    # two in a line +2
    evaluation += p1_lines_of_two * lines_of_two_multiplier
    evaluation -= p2_lines_of_two * lines_of_two_multiplier

    # three in a line +4
    evaluation += p1_lines_of_three * lines_of_three_multiplier
    evaluation -= p2_lines_of_three * lines_of_three_multiplier

    # piece in middle +5
    for row in range(board_height):
        if board[row][3] == 1:
            evaluation += middle_multiplier
        elif board[row][3] == 2:
            evaluation -= middle_multiplier

    # win +1000
    if check_win(board) == 1:
        evaluation += math.inf
    elif check_win(board) == 2:
        evaluation -= math.inf

    return evaluation


def analyse_move(player, column, board):
    if check_win(board) != 0:
        return board

    analysis_board = copy.deepcopy(board)

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


def print_board(board):
    print()

    for y in range(board_height):
        for x in range(board_width):
            if board[y][x] == 0:
                print("_ ", end="")

            elif board[y][x] == 1:
                print("X ", end="")

            else:
                print("O ", end="")

        print("\n")

    print("1 2 3 4 5 6 7")


def is_legal(move, board):
    if move < 1 or move > 7:
        return False

    # Check if the column is full
    elif board[0][move - 1] != 0:
        return False

    else:
        return True


def legal_moves(board):
    moves = []

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, board):
            moves.append(i)

    return moves


def pieces_per_line(player, board):
    lines_of_two = 0
    lines_of_three = 0

    # Check horizontal rows
    for y in range(board_height):
        for x in range(board_width - 3):
            line = board[y][x:x + 4]

            piece_count = 0

            for piece in line:
                if piece == player:
                    piece_count += 1
                elif piece != player and piece != 0:
                    break

            if piece_count == 2:
                lines_of_two += 1
            elif piece_count == 3:
                lines_of_three += 1

    # Check vertical rows
    for x in range(board_width):
        for y in range(board_height - 3):
            line = [board[y][x], board[y+1][x], board[y+2][x], board[y+3][x]]

            piece_count = 0

            for piece in line:
                if piece == player:
                    piece_count += 1
                elif piece != player and piece != 0:
                    break

            if piece_count == 2:
                lines_of_two += 1
            elif piece_count == 3:
                lines_of_three += 1

    # Check descending diagonal rows
    for y in range(board_height - 3):
        for x in range(board_width - 3):
            line = [board[y][x], board[y + 1][x + 1], board[y + 2][x + 2], board[y + 3][x + 3]]

            piece_count = 0

            for piece in line:
                if piece == player:
                    piece_count += 1
                elif piece != player and piece != 0:
                    break

            if piece_count == 2:
                lines_of_two += 1
            elif piece_count == 3:
                lines_of_three += 1

    # Check ascending diagonal rows
    for y in range(3, board_height):
        for x in range(board_width - 3):
            line = [board[y][x], board[y - 1][x - 1], board[y - 2][x - 2], board[y - 3][x - 3]]

            piece_count = 0

            for piece in line:
                if piece == player:
                    piece_count += 1
                elif piece != player and piece != 0:
                    break

            if piece_count == 2:
                lines_of_two += 1
            elif piece_count == 3:
                lines_of_three += 1

    return lines_of_two, lines_of_three


def check_win(board):
    piece_count = 1

    # Check horizontal rows
    for y in range(board_height):
        for x in range(board_width - 1):
            if board[y][x] == board[y][x + 1] and board[y][x] != 0:
                piece_count += 1

                if piece_count >= 4:
                    return board[y][x]

            else:
                piece_count = 1

        piece_count = 1

    # Check vertical rows
    for x in range(board_width):
        for y in range(board_height - 1):
            if board[y][x] == board[y + 1][x] and board[y][x] != 0:
                piece_count += 1

                if piece_count >= 4:
                    return board[y][x]

            else:
                piece_count = 1

        piece_count = 1

    # Check descending diagonal rows
    for y in range(board_height - 3):
        for x in range(board_width - 3):
            if board[y][x] == board[y + 1][x + 1] == board[y + 2][x + 2] == board[y + 3][x + 3] and board[y][x] != 0:

                return board[y][x]

    # Check ascending diagonal rows
    for y in range(3, board_height):
        for x in range(board_width - 3):
            if board[y][x] == board[y - 1][x + 1] == board[y - 2][x + 2] == board[y - 3][x + 3] and board[y][x] != 0:

                return board[y][x]

    return 0
