def sum(nums, target):
    d_list = {}
    for index, x in enumerate(nums):
        if x in d_list:
            return [d_list[x], index]
        else:
            d = target - x
            d_list[d] = index

x = sum([2, 7, 11, 15], 9) # asd
print(x)