def find_median(n):
    mid = len(n)//2
    if len(n)%2 == 0:
        return (n[mid] + n[mid-1])/2
    else:
        return n[mid]

def findMedianSortedArrays(nums1, nums2):
    x = find_median(nums1)
    y = find_median(nums2)
    if len(nums1) == 0:
        return y
    if len(nums2) == 0:
        return x
    return (x+y)/2

x = findMedianSortedArrays([], [7])
print(x)