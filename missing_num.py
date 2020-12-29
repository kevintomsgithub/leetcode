def missingNumber(nums):
    if len(nums) == 1 : return 1
    n = len(nums)
    total = (n*(n+1))//2
    print(f'total: {total}')
    s = sum(nums)
    print(f'sum: {s}')
    return total - s

n = [1]
print(missingNumber(n))