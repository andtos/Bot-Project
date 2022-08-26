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

while not isOver:
    printBoard(board)
    if(playerTurn):
        row = int(input('Player 1: Enter chosen row'))
        col = int(input('Player 1: Enter chosen column'))
        board[row][col] = 1
    else:
        row = int(input('Player 2: Enter chosen row'))
        col = int(input('Player 2: Enter chosen column'))
        board[row][col] = 2
    
    playerTurn = not playerTurn
    gameCount = gameCount + 1
    if(gameCount >= 9):
        isOver = True
