# Create matrix to play connect four on the command line
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def place_peice(board, row, col, piece):
    board[row][col] = piece


def is_valid_move(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def win(board, piece):
    # horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # positive slope
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # negative slope
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = create_board()
print_board(board)
game_over = False
turn_number = 0

while not game_over:
    # Ask for input of player one
    if turn_number == 0:
        col = int(input("It is your move player 1! Pick a row. (0-6):"))

        if is_valid_move(board, col):
            row = get_open_row(board, col)
            place_peice(board, row, col, 1)

            if win(board, 1):
                print('The underdog takes it! Player one is the victor! Genius! *photoflash* Can I get your autograph?')
                game_over = True


    # Ask for input of player two
    else:
        col = int(input("It is your move player 2! Pick a row. (0-6):"))

        if is_valid_move(board, col):
            row = get_open_row(board, col)
            place_peice(board, row, col, 2)

            if win(board, 2):
                print('Lucky. Player two wins. Could\'ve gone either way. Bad refereeing.')
                game_over = True



    print_board(board)

    turn_number += 1
    turn_number = turn_number % 2
