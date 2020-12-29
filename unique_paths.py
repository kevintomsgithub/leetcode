def uniquePaths(m, n):
    def helper(i=0, j=0, mem={}):
        if str([i,j]) in mem:
            return mem[str([i, j])]
        if i > m or j > n:
            return 0
        if i == m-1 and j == n-1:
            return 1
        ways_down = helper(i+1, j)
        ways_right = helper(i, j+1)
        mem[str([i, j])] = ways_down + ways_right
        return mem[str([i, j])]
    return helper()

def uniquePaths_btm_up(m, n):
    matrix = [[0]*n for _ in range(m)]
    for i in range(n):
        matrix[0][i] = 1
    for i in range(m):
        matrix[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[m-1][n-1]

print(uniquePaths_btm_up(7, 3))