

global N
N = 4

def printSol(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board, row, col):
    for i in range(N):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQ(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQ(board, col+1):
                return True
            board[i][col] = 0
    return False

def solveN():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    if solveNQ(board, 0) == False:
        return False
    printSol(board)
    return True
solveN()
