
def selection_sort(array):
    array_len = len(array)
    for i in range(array_len):
        curr_pos = i
        for j in range(i, array_len):
            if array[j] < array[curr_pos]:
                curr_pos = j
        temp = array[i]
        array[i] = array[curr_pos]
        array[curr_pos] = temp
    return array

array = [4, 2, 3, 5, 6, 8, 1]
x = selection_sort(array)
print(x)