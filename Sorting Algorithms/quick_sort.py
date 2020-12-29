def quicksort(a):
    if len(a) <= 1: return a
    smaller, equal, larger = [], [], []
    middle_pos = len(a)//2
    pivot=a[middle_pos]

    for x in a:
        if x < pivot: smaller.append(x)
        elif x == pivot: equal.append(x)
        else: larger.append(x)

    return quicksort(smaller)+equal+quicksort(larger)

array = [4,7,8,6,4,3,5,7]
x = quicksort(array)
print(x)