import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))

    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_loc(board, col):
    return board[5][col] == 0

def get_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def print_board(board):
    print(np.flip(board, 0))

board = create_board()
game_over = False
turn = 0

# print(board)

while not game_over:
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6): "))

        if is_valid_loc(board, col):
            row = get_open_row(board, col)
            drop_piece(board, row, col, 1)

    else:
        col = int(input("Player 2 Make your Selection (0-6): "))

        if is_valid_loc(board, col):
            row = get_open_row(board, col)
            drop_piece(board, row, col, 2)

    turn += 1
    turn %= 2

    print_board(board)
