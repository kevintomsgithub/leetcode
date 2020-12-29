def merge(L, R):
    final_array = []
    i, j = 0, 0
    while i<len(L) and j<len(R):
        if L[i] < R[j]:
            final_array.append(L[i])
            i += 1
        else:
            final_array.append(R[j])
            j += 1
    final_array += L[i:]
    final_array += R[j:]
    return final_array

def merge_sort(a):
    if len(a) <= 1: return a
    left, right =  merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])
    return merge(left, right)

array = [9, 11, 7, 15, 2, 4, 8, 3, 7, 5, 7]
x = merge_sort(array)
print(x)