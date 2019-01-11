# CONNECT FOUR

import jari
import jari2

from matplotlib import pyplot as plt

board_width = 7
board_height = 6

jari1_wins = 0
jari2_wins = 0
amount_of_ties = 0

played_moves = []


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
    global board
    board = make_board(board_width, board_height)

    global amount_of_ties

    while True:
        move = jari.calculate_move(board)
        play_move(1, move)

        played_moves.append(move)

        if check_win(board):
            global jari1_wins
            jari1_wins += 1
            return

        if is_tied(board):
            amount_of_ties += 1
            return

        move = jari2.calculate_move(board)
        play_move(2, move)

        played_moves.append(move)

        if check_win(board):
            global jari2_wins
            jari2_wins += 1
            return

        if is_tied(board):

            amount_of_ties += 1
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


board = make_board(board_width, board_height)

for i in range(100):
    play_game()

print("jari1 wins: " + str(jari1_wins))
print("jari2 wins: " + str(jari2_wins))
print("ties: " + str(amount_of_ties))

plt.hist(played_moves)
plt.show()
