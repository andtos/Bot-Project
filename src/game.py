from array import *;
board = [[0,0,0], [0,0,0], [0,0,0]]
print( board)
isOver= False
playerTurn = True
row = 0
column = 0
gameCount = 0

def printBoard(board):
    for row in range(len(board)):
        print(board[row])

def win(board):
    if(board[0][0] == board [0][1] == board[0][2]):
        return board[0][0] 
    if(board[1][0] == board [1][1] == board[1][2]):
        return board[1][0]
    if(board[2][0] == board [2][1] == board[2][2]):
        return board[2][0]
    if(board[0][0] == board [1][0] == board[2][0]):
        return board[0][0]
    if(board[0][1] == board [1][1] == board[2][1]):
        return board[0][1]
    if(board[0][2] == board [1][2] == board[2][2]):
        return board[0][2]
    if(board[0][0] == board [1][1] == board[2][2]):
        return board[0][0]
    if(board[2][0] == board [1][1] == board[0][2]):
        return board[2][0]
    return 0

while not isOver:
    printBoard(board)
    if(playerTurn):
        row = int(input('Player 1: Enter chosen row: '))
        col = int(input('Player 1: Enter chosen column: '))
        if(board[row][col] == 0 and row > -1 and row < 3 and col > -1 and col < 3):
            board[row][col] = 1
        else:
            print('Invalid Entry, please try again.')
            continue

    else:
        row = int(input('Player 2: Enter chosen row: '))
        col = int(input('Player 2: Enter chosen column: '))
        if(board[row][col] == 0 and row > -1 and row < 3 and col > -1 and col < 3):
            board[row][col] = 2
        else:
            print('Invalid Entry, please try again.')
            continue
    
    playerTurn = not playerTurn
    x = win(board)
    gameCount += 1
    
    if(x > 0 ):
        isOver = True
        print("Winner is: " + str(x))
    elif(gameCount == 9):
        isOver = True
        print("Tie")
printBoard(board)