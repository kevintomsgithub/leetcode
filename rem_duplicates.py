def removeDuplicates(nums):
    i = j = 0
    while i < len(nums)-1 and j < len(nums):
        j += 1
        if nums[i] == nums[j]:
            del nums[j]
            j -= 1
        else:
            i = j
    return nums

a = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(a))