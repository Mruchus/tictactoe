# √ choose the players
# √ create a board
# √ choose an initial player
# - until someone wins
# √ show board
# √ choose location, mark it
# activate player
# game over


def is_draw(board, round):
    return round == 9 and not find_winner(board)


def main():
    #Board is a list of rows
    #Rows is a list of cells

    board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

    # CHOOSE THE ACTIVE PLAYER
    active_player_index = 0
    players = ["PLAYER1", "PLAYER2"]
    symbols = ["X", "O"]
    player = players[active_player_index]

    round = 0
    # UNTIL SOMEONE WINS
    while not (find_winner(board) or is_draw(board, round)):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player, symbol)
        show_board(board)
        if choose_location(board, symbol):
            round += 1
        else:
            print("That isn't an option, try again")
            continue



        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index+1) % len(players)

    print()
    if is_draw(board, round):
        print("It's a draw !")
    else:
        print(f"Game over! {player} has won with the player")
    print()
    show_board(board)



def choose_location(board, symbol):
    print()
    rowcol = input("Choose which position (row, column): ")
    if len(rowcol) != 2:
        return False

    row = int(rowcol[0])-1
    column = int(rowcol[1])-1

    print(row, column)
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True

def show_board(board):
    print('   '+''.join([f'|  {i+1}  ' for i in range(3)])+'|')
    for i, row in enumerate(board):
        print(f"{i+1}  |  ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end="  |  ")
        print()

def announce_turn(player, symbol):
    print()
    print(f"It's {player}[{symbol}]'s turn. Here is the board:")
    print()


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # WIN BY ROWS
    rows = board
    sequences.extend(rows)

    #WIN BY COLUMNS
    for col_index in range(0,3):
        col = [
            board[0][col_index],
            board[1][col_index],
            board[2][col_index]
            ]
    sequences.append(col)

    # WIN BY DIAGONALS
    diagonals = [
        [board[0][0],board[1][1],board[2][2]],
        [board[0][2],board[1][1],board[2][0]]
    ]
    sequences.extend(diagonals)

    return sequences

# bug scenario
#  |  1  |  2  |  3  |
# 1  |  O  |  _  |  _  |
# 2  |  X  |  X  |  O  |
# 3  |  _  |  _  |  _  |
#
# Choose which position (row, column): 13

# draw bug
# Game over! PLAYER1 has won with the player
#    |  1  |  2  |  3  |
# 1  |  X  |  O  |  O  |
# 2  |  O  |  X  |  X  |
# 3  |  X  |  X  |  O  |

if __name__ == '__main__':
    main()




