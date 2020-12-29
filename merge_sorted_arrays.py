def merge(nums1, m, nums2, n):
    i=m-1;j=n-1;k=len(nums1)-1
    while j >= 0:
        if nums2[j] >= nums1[i]: 
            nums1[k] = nums2[j]
            j -= 1; k -= 1
        elif nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1; i -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)