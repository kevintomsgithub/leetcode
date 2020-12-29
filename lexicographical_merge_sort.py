def merge(left, right):
    i=j=0
    sorted_array = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else: 
            sorted_array.append(right[j])
            j += 1
    sorted_array += left[i:]
    sorted_array += right[j:]
    return sorted_array
        
def lexicographical(a):
    if len(a) == 1: return a
    mid = len(a)//2
    l = lexicographical(a[:mid])
    r = lexicographical(a[mid:])
    return merge(l, r)

array = ['azin', 'akin', 'abin', 'aain']
# array = [8, 9, 1, 4, 2, 3]
print(lexicographical(array))