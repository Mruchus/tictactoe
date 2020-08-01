import numpy as np
import pygame
import sys
import math

# constants
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

#functions

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


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):

            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS )


    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):

            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS )

            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS )


    pygame.display.update()



# game doesn't end until someone wins and so it turns True
board = create_board()
print()
print_board(board)
print()
game_over = False
player_turn = 0

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 60)



# main program

def draw_top_piece(event, player_turn):
    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
    posx = event.pos[0]
    if player_turn == 0:
        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
    else:
        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

def draw_label(text, color):
    label = myfont.render(text, 1, color)
    screen.blit(label, (40,10))

while True:

    while not game_over:

        for event in pygame.event.get():
            correct_move = False

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                draw_top_piece(event, player_turn)

            if event.type == pygame.MOUSEBUTTONDOWN and \
                    (pygame.mouse.get_pressed() ==  (1, 0, 0) or
                     pygame.mouse.get_pressed() ==  (0, 0, 1)):

                if player_turn == 0:
                    posx =event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        correct_move = True

                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            draw_label("Player 1 WINS!", RED)
                            game_over = True

                #ask for player 2 input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        correct_move = True
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            draw_label("Player 2 WINS!", YELLOW)
                            game_over =  True


                if correct_move:
                    player_turn += 1
                    player_turn = player_turn % 2

                    print()
                    print_board(board)
                    draw_board(board)
                    draw_top_piece(event, player_turn)
                    print()
                else:
                    draw_label("Wrong move. Try again!", BLUE)
                    pygame.display.update()

    #start again
    game_over = False
    board = create_board()
    draw_board(board)










