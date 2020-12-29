def max_sub_array(array):
    curr_sum = max_sum = array[0]
    for i in array[1:]:
        curr_sum = max(i, curr_sum+i)
        max_sum = max(curr_sum, max_sum)
    return max_sum

def sum_of_array(array, i):
    if i == 0: return array[i]
    else:
        return sum_of_array(array, i-1) + array[i]

a = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(a))