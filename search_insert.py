def binary_search(n, target):
    i = 0; j = len(n)
    while i+1 < j:
        mid = (i+j) // 2
        if n[mid] == target:
            return mid
        elif target < n[mid]:
            j = mid
        else:
            i = mid
    return mid if target < n[-1] else mid +1

def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i+1

a = [1, 3, 5, 6]
x = binary_search(a, 10)
print(x)
