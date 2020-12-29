def maxCoins_old(nums):
    profit = []
    def helper(a, profits_sub=[]):
        if len(a) == 1: return sum(profits_sub)
        local_profits = []
        for pivot in range(len(a)):
            curr_profit = 0
            left=pivot-1; right=pivot+1
            if pivot - 1 < 0 and pivot + 1 > len(a):
                curr_profit += a[pivot]
            elif pivot - 1 < 0:
                curr_profit += a[pivot] * a[right]
            elif pivot + 1 > len(a)-1:
                curr_profit += a[pivot] * a[left]
            else:
                curr_profit += a[left] * a[pivot] * a[right]
            new_a = a[:pivot] + a[pivot+1:]
            profits_sub.append(curr_profit)
            local_profits.append(helper(new_a, profits_sub))
            profits_sub.pop()
            profit.append(max(local_profits))
        return max(local_profits)
    return helper(nums)


def maxCoins(nums):
    nums = [1]+nums+[1]
    def helper(left, right):
        if right - left < 2: ans = 0
        else:
            ans = 0
            for i in range(left+1, right):
                cost = nums[left] * nums[i] * nums[right]
                ans = max(ans, cost + helper(left, i), helper(i, right))
        return ans
    return helper(0, len(nums)-1)

a = [3, 1, 5, 8]
print(maxCoins(a))