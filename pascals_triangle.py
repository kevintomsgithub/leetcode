def generate_pascals_triangle(n):
    if n == 0: return []
    if n == 1: return [1]
    dp = [[1], [1, 1]]
    for i in range(2, n):
        temp = []
        for j in range(len(dp[i-1])-1):
            temp.append(dp[i-1][j] + dp[i-1][j+1])
        dp.append([1] + temp + [1])
    return dp

n = 2
print(generate_pascals_triangle(n))