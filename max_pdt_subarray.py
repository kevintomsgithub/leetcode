def maxProduct(nums):
    if len(nums) == 1: return 0
    def helper(i=0):
        if i == len(nums)-2: return nums[i] * nums[i+1]
        return max(nums[i], nums[i]*helper(i+1))
    return helper()

# a = [2, 3, -2, 4]
a = [2, 3]

print(maxProduct(a))