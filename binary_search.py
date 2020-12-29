def binary_search_itr(n, target):
    if len(n) == 0: return False
    i = 0; j = len(n) - 1
    while i<=j:
        mid = (i+j)//2
        if n[mid] == target:
            return mid
        elif target < n[mid]:
            j = mid
        else:
            i = mid
    return False

def binary_search_rec(n, target, l, r):
    if l > r:
        return False
    mid = (l+r)//2
    if n[mid] == target:
        return mid
    elif target < n[mid]:
        return binary_search_rec(n, target, l, mid-1)
    else:
        return binary_search_rec(n, target, mid+1, r)

a = [i for i in range(10)]
print(binary_search_rec(a, 5, 0, len(a)-1))