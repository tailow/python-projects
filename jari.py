# CONNECT 4 BOT

import random
import copy


def calculate_move(board):
    analysis_board = copy.deepcopy(board)

    board_width = len(board[0])

    legal_moves = []

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, analysis_board):
            legal_moves.append(i)

    # Check for winning moves
    if is_checkmate(2, analysis_board, board):
        return is_checkmate(2, analysis_board, board)

    # Check for opponent winning moves
    if is_checkmate(1, analysis_board, board):
        return is_checkmate(1, analysis_board, board)

    if is_legal(4, board):
        return 4

    else:
        return random.choice(legal_moves)


def analyse_move(player, column, analysis_board, board):

    board_height = len(board)

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


def is_legal(move, board_state):

    if move < 1 or move > 7:
        return False

    # Check if the column is full
    elif board_state[0][move - 1] != 0:
        return False

    else:
        return True


def is_checkmate(player, analysis_board, board):
    board_width = len(board[0])

    legal_moves = []

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, analysis_board):
            legal_moves.append(i)

    # For each move, check if there is a win
    for move in legal_moves:
        analysis_board = copy.deepcopy(board)

        # Play a move in the analysis board and check if the game is over
        if check_win(analyse_move(player, move, analysis_board, board)):
            return move


def check_win(board_state):
    piece_count = 1

    board_width = len(board_state[0])
    board_height = len(board_state)

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
