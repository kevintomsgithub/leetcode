import random

class Solution:

    def __init__(self, nums):
        self.array = nums
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.array
        
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        print('Org array : ', self.array)
        temp = self.array
        for i in range(len(temp)):
            swap_index = random.randrange(i, len(temp))
            temp[i], temp[swap_index] = temp[swap_index], temp[i]
        return temp

nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_3 = obj.reset()
print(param_3)