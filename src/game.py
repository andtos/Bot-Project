from array import *;
board = [[0,0,0], [0,0,0], [0,0,0]]
print( board)
isOver= False
playerTurn = True
row = 0
column = 0
gameCount = 0
while not isOver:
    if(playerTurn):
        row = input('Player 1: Enter chosen row')
        col = input('Player 1: Enter chosen column')
        board[row][col] = 1
    else:
        row = input('Player 2: Enter chosen row')
        col = input('Player 2: Enter chosen column')
        board[row][col] = 2
    
    playerTurn = not playerTurn
    gameCount = gameCount + 1
    if(gameCount >= 9):
        isOver = True
