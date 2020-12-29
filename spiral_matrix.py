def spiralOrder(matrix):
    result = []
    rows = len(matrix) - 1 
    cols = len(matrix[0]) - 1
    for i in range((rows+2)//2):
        # top-row
        for j in range(i, cols-i+1):
            result.append(matrix[i][j])
        # right-col
        for j in range(i+1, rows-i+1):
            result.append(matrix[j][rows-i])
        # bottom-row
        for j in range(cols-i-1, i-1, -1):
            print(f'i:{i}, j:{j}')
            result.append(matrix[cols-i][j])
        # left-col
        for j in range(rows-i-1, i, -1):
            result.append(matrix[j][i])
    return result

a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
b = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(spiralOrder(b))