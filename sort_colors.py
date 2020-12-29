def sortColors(nums):
    result = []
    count = [0, 0, 0]
    for i in nums:
        count[i] += 1
    for index, i in enumerate(count):
        result += [index]*i
    return result

def sortColors_inplace(nums):
    zero_pointer = 0
    two_pointer = len(nums)-1
    i = 0
    # 0, 1, 0, 2, 1
    while i < len(nums):
        if nums[i] == 0:
            nums[i], nums[zero_pointer] =  nums[zero_pointer], nums[i]
            zero_pointer += 1
        elif nums[i] == 2:
            nums[i], nums[two_pointer] =  nums[two_pointer], nums[i]
            two_pointer -= 1
        i += 1

a = [2,0,2,1,1,0]
sortColors_inplace(a)
print(a)