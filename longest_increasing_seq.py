def lengthOfLIS(nums):
    nums.sort()
    prev = nums[0]; length = 0; curr_length = 0
    for i in range(1, len(nums)):
        if nums[i] > prev:
            curr_length += 1
        else:
            length = curr_length
            curr_length = 0
        prev = nums[i]
    return length

def lengthOfLIS_normal(nums):
    if len(nums) == 1: return 1
    max_len = 0
    for i in range(len(nums)-1):
        curr_len = 1
        prev = nums[i]
        for j in range(i+1, len(nums)):
            if prev < nums[j]:
                curr_len += 1
                prev = nums[j]
        if curr_len > max_len: max_len = curr_len
    return max_len

def lengthOfLIS_rec(nums):
    if len(nums) == 0: return 0
    def helper(i, prev):
        if i < 0: return 0
        if nums[i] >= prev: 
            return helper(i-1, nums[i])
        else:
            l = helper(i-1, nums[i]) + 1
            r = helper(i-1, prev)
            return max(l ,r)
    return helper(len(nums)-2, nums[-1]) + 1

def lengthOfLIS_dp(nums):
    if len(nums) == 0: return 0
    a = [1 for i in nums]
    i=0; j=1
    while j < len(nums)-1:
        if i == j+1: i=0; j+=1
        if nums[i] < nums[j]: a[j] = a[i] + 1
        else: a[j] = a[i]
        i += 1
    return max(a)+1


# array = [5, 6, 7, 8, -1, -2, 7]
array = [10,9,2,5,3,7,101,18]
# array = [4,10,4,3,8,9]
print(lengthOfLIS_dp(array))
print(lengthOfLIS_rec(array))