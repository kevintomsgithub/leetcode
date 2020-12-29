
def kadane(array):
    curr_max = global_max = array[0]
    mem = [curr_max]
    global_max_index = 0
    for i in range(1, len(array)):
        curr_max = max(array[i], curr_max+array[i])
        mem.append(curr_max)
        if curr_max > global_max:
            global_max_index = i
            global_max = curr_max
    # Finding the best pair
    sub_array = [array[global_max_index]]
    for i in range(global_max_index-1, -1, -1):
        sub_array.append(array[i])
        if array[i] == mem[i]:
            break
    sub_array.reverse()

    return global_max, sub_array


array = [-1, -2, 1, 2, 3, 3, -2]
x, y = kadane(array)
print('Greatest sub sum obtained: ', x)
print('The pair that obtains the greatest sum: ', y)