def minPathSum(grid):
    #First row
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]
    #First column
    for j in range(1, len(grid)):
        grid[j][0] += grid[j-1][0]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])  
    print(grid)
    return grid[-1][-1]

def minPathSum_recursive(grid):
    mem = {}
    def helper(i, j):
        if i == len(grid) or j == len(grid[0]):
            return float('inf')
        if i == len(grid)-1 and j == len(grid[0])-1: 
            return grid[i][j]
        if (i, j) in mem: 
            return mem[(i, j)]
        mem[(i, j)] = grid[i][j] + min(helper(i+1, j), helper(i, j+1))
        return mem[(i, j)]

    return helper(0, 0)

# grid = [[1,2,3],[4,5,6]]
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum_recursive(grid))

'''
[1,2,3]
[4,5,6]
'''