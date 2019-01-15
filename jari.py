# CONNECT 4 BOT

import copy

board_height = 6
board_width = 7


def calculate_move(board, player, opponent):
    analysis_board = copy.deepcopy(board)

    legal_moves = []

    best_move = -1
    best_move_evaluation = -200

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, analysis_board):
            legal_moves.append(i)

    # Check evaluation of each move
    for move in legal_moves:
        analysis_board = copy.deepcopy(board)

        evaluation = evaluate(analyse_move(player, move, analysis_board), player, opponent)

        print(evaluation)

        if evaluation > best_move_evaluation:
            best_move = move
            best_move_evaluation = evaluation

    print("evaluation: " + str(evaluate(board, player, opponent)))

    return best_move


def evaluate(board, player, opponent):
    evaluation = 0

    analysis_board = copy.deepcopy(board)
    legal_moves = []

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, board):
            legal_moves.append(i)

    if check_win(board) == player:
        evaluation = 100

    elif is_checkmate(opponent, board):
        evaluation = -100

    evaluation += pieces_in_column(4, player, opponent, board) * 3

    evaluation += pieces_in_column(3, player, opponent, board) * 2

    evaluation += pieces_in_column(5, player, opponent, board) * 2

    return evaluation


def pieces_in_column(column, player, opponent, board):
    own_pieces = 0
    opponent_pieces = 0

    for y in range(board_height):
        if board[y][column - 1] == player:
            own_pieces += 1

        elif board[y][column - 1] == opponent:
            opponent_pieces += 1

    evaluation = own_pieces - opponent_pieces

    return evaluation


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


def is_legal(move, board_state):
    if move < 1 or move > 7:
        return False

    # Check if the column is full
    elif board_state[0][move - 1] != 0:
        return False

    else:
        return True


def is_checkmate(player, board):
    legal_moves = []

    # Check legal moves
    for i in range(board_width + 1):
        if is_legal(i, board):
            legal_moves.append(i)

    # For each move, check if there is a win
    for move in legal_moves:
        analysis_board = copy.deepcopy(board)

        # Play a move in the analysis board and check if the game is over
        if check_win(analyse_move(player, move, analysis_board)):
            return move


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
