def canJump(nums):
    def helper(i=0):
        if i == len(nums)-1: return True
        if i >= len(nums): return False
        ans = []
        for j in range(nums[i]):
            ans.append(helper(i+j+1))
        return any(ans)
    return helper()

def canJump_greedy(nums):
    last_pos = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= last_pos: last_pos = i
    return last_pos == 0
        
# a = [2,3,1,1,4]
a = [3,2,1,0,4]
# print(canJump(a))
print(canJump_greedy(a))