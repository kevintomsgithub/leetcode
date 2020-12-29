def pal(x):
    arr = str(x)
    if len(arr)%2 == 0:
        return False
    back_ptr = len(arr)-1
    for front_prt in range(len(arr)):
        if arr[front_prt] != arr[back_ptr - front_prt]:
            return False
    return True

s = 112111
print(pal(s))