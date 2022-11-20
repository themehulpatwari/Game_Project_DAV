import os

# Board Setup for the game.
BOARD =[
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

# Printing the board.
def print_board(board):
    print()
    print('Please Choose your column between 0 to 6')
    print('- - - - - - - - - - - - - - - - - - - - - ')
    print(' 0  1  2  3  4  5  6  ')
    print('- - - - - - - - - - - - - - - - - - - - - \n')
    for k in range(len(board)):
        print(board[k])

# Dropping the piece in vacant column.
def move(board, position, symbol):
    global BOARD
    for i in range(len(board)-1, -1, -1):
        if board[i][position] == 0:
            board[i][position] = symbol
            board = BOARD
            break

# Checking whether the column is already full or not.
def board_valid(board, position):
    for i in range(len(board)-1, -1, -1):
        if board[i][position] == 0:
            break
            return 1
    else:
        return 0



# Defining a function to check whether any combiantion for the win is possible or not.
def win(board):
    for i in range(len(board)):
        # Iterating over rows to determine a win.
        for j in range(4):
            if (board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]) == True and board[i][j] != 0:
                return True
        # Iterating over columns to determine a win.
        for j in range(3):
            if (board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i]) == True and board[j][i] != 0:
                return True

    for i in range(3):
        # Checking for a combination in negative sloped diagonal.
        for j in range(4):
            if (board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]) == True and board[i][j] != 0:
                return True
        # Checking for a combination in positive sloped diagonal.
        for j in range(3,7):
            if (board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]) == True and board[i][j] != 0:
                return True

# Game Interface
def connect4_main():
    print('Player 1 = 1\nPlayer 2 = 2')
    print_board(BOARD)
    turn =  1

    while True:
        if turn % 2 == 0:
            player = 'Player 2'
            symbol = 2
        else:
            player = 'Player 1'
            symbol = 1

        while True:
            player_choice = int(input('\nWhat is your move {}: '.format(player)))
            os.system('cls')
            if board_valid(BOARD, player_choice) == 0:
                print('Column Full')
            else:
                move(BOARD, player_choice, symbol)
                print_board(BOARD)
                turn += 1
                break
        if win(BOARD):
            print('\n{} has won the game'.format(player))
            break

if __name__ == "__main__":
    connect4_main()
