# √ choose the players
# √ create a board
# √ choose an initial player
# - until someone wins
# √ show board
# √ choose location, mark it
# activate player
# game over


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

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again")
            continue



        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index+1) % len(players)

    print()
    print(f"Game over! {player} has won with the player")



def choose_location(board, symbol):
    print()
    row = int(input("Choose which row: "))
    column = int(input("Choose which column: "))


    row -= 1
    column -= 1
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
    for row in board:
        print("  |  ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end="  |  ")
        print()

def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here is the board:")
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
        [board[0][2],board[1][1],board[1][0]]
    ]
    sequences.extend(diagonals)

    #daddy adds some new stuff
    
    return sequences





if __name__ == '__main__':
    main()




