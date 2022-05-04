def rec(arr, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = rec(arr, total, i-1)
    else:
        to_return = rec(arr, total-a[i], i-1) + rec(arr, total, i-1)
    return to_return

def count_set(arr, total):
    return rec(arr, total, len(arr)-1)


a = [2, 4, 6, 10]
total = 16

print(count_set(a, total))