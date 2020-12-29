def moveZeroes(nums):
    i=0; last_found_zero=len(nums)-1
    while i < last_found_zero:
        if nums[i] == 0:
            nums[i], nums[last_found_zero] = nums[last_found_zero], nums[i]
            i += 1; last_found_zero -= 1
        else: i+=1

a = [0,1,0,3,12]
moveZeroes(a)
print(a)