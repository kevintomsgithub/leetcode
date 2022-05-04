def minCostClimbingStairs(cost):
    cost = [0] + cost
    mem = {}
    def helper(i):
        if i >= len(cost): return 0
        if i in mem: return mem[i]
        mem[i] = cost[i] + min(helper(i+1), helper(i+2))
        return mem[i]
    return helper(0)

def minCostClimbingStairs_dp(cost):
    dp = [0 for _ in range(len(cost))]
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[-1], dp[-2])


cost = [10, 15, 20]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

print(minCostClimbingStairs_dp(cost))