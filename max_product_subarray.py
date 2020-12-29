def maxProduct(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    dp = [0 for i in nums]
    dp[0] = nums[0]
    i = 0 
    while i<len(nums):
        if dp[i-1] == 0: dp[i] = nums[i]
        else: dp[i] = dp[i-1]*nums[i]
        i += 1
    print(dp)
    return max(dp)

n = [3, -1, 4]
print(maxProduct(n))