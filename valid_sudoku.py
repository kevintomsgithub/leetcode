def isValidSudoku(board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != '.':
                # check for row
                for i in range(cols):
                    if board[row][col] == board[row][i] and i != col: return False
                # check for col
                for i in range(rows):
                    if board[row][col] == board[i][col] and i != row: return False
                # check for sub grid
                x1 = (row//3)*3; y1 = (col//3)*3
                x2 = x1+3; y2 = y1+3
                for i in range(x1, x2):
                    for j in range(y1, y2):
                        if board[row][col] == board[i][j] and \
                        i != row and j != col: return False
    return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board))