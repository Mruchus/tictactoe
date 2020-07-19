import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

# creating a board: 6 rows by seven columns, filled with zeros, array form

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    #where the piece should drop
    board[row][col] = piece


def is_valid_location(board, col):
    # checking the top row of the board to see if there is an empty slot
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board,col):
    # checking every row in the board's column for a free slot
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            # returns the row number in which the row contains a 0
            return r

def print_board(board):
    # flipping the board so (0,0) will be at the bottom left
    print(np.flip(board, 0))

def winning_move(board, piece):
    # checking for horizontal wins
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            # check for 4 pieces in a row
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for wins
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            # check for 4 pieces in a row
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check for positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT - 3):
            # check for 4 pieces in a row
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True


    # Check for negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            # check for 4 pieces in a row
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True




# game doesn't end until someone wins and so it turns True
board = create_board()
print()
print_board(board)
print()
game_over = False
turn = 0


while not game_over:
    # ask for Player 1's input - where do they want to go?
    if turn == 0:

        col = int(input("Player 1, make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board,col)
            drop_piece(board, row, col, 1)


            if winning_move(board, 1):
                print()
                print(" Player 1, YOU WIN!")
                game_over = True

    #ask for player 2 input
    else:

        col = int(input("Player 2, make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board,col)
            # note: '2' is taken in as the 'piece' here
            drop_piece(board, row, col, 2)

    print()
    print_board(board)
    print()

    turn += 1
    turn = turn % 2


