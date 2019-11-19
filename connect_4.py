import numpy as np

PIECE_ONE = 1
PIECE_TWO = 2
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))

    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_loc(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def print_board(board):
    print(np.flip(board, 0))

def check_win(board, piece):
    # Checking Horizontally
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Checking Vertically
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Checking Positively sloped diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Checking Positively sloped diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()
game_over = False
turn = 0

# print(board)

while not game_over:
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6): "))

        if is_valid_loc(board, col):
            row = get_open_row(board, col)
            drop_piece(board, row, col, PIECE_ONE)

            if check_win(board, PIECE_ONE):
                print("Player One Wins")
                game_over = True


    else:
        col = int(input("Player 2 Make your Selection (0-6): "))

        if is_valid_loc(board, col):
            row = get_open_row(board, col)
            drop_piece(board, row, col, PIECE_TWO)

            if check_win(board, PIECE_TWO):
                print("Player Two Wins")
                game_over = True

    turn += 1
    turn %= 2

    print_board(board)
