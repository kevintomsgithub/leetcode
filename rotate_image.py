def rotate(matrix):
    rows = len(matrix)-1
    cols = len(matrix[0])-1
    for i in range((rows+1)//2):
        for j in range(i, cols-i):
            matrix[i][j], matrix[j][cols-i] = matrix[j][cols-i], matrix[i][j]
            matrix[i][j], matrix[rows-i][cols-j] = matrix[rows-i][cols-j], matrix[i][j]
            matrix[i][j], matrix[rows-j][i] = matrix[rows-j][i], matrix[i][j]

m = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15,14,12,16]
]
'''
# Expected
[
    [15,13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7,10,11]
]
# Output obtained
[
    [15, 12, 2, 5],
    [14, 3, 4, 13],
    [10, 6, 8, 9],
    [16, 7, 1, 11]
]
'''
rotate(m)
print(m)