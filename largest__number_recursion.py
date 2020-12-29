def find_largest():
    array = [6, 2, 9, 8, 11, 15, 1, 3]
    value = 17
    ans = []
    def helper(i):
        if i == 0:
            return array[i]
        else:
            curr_largest = array[i]
            temp = helper(i-1)
            return max(curr_largest, temp)
    
    def divide_and_conquer(i, j):
        if i == j:
            return array[i]
        else:
            mid = (i+j)//2
            left = divide_and_conquer(i, mid)
            right = divide_and_conquer(mid+1, j)
            return left if left > right else right

    def sum_pairs(i):
        if i < 0:
            return 0
        else:
            temp = array[i]
            temp1 = sum_pairs(i-1)
            temp2 = sum_pairs(i-2)
            temp_sum = temp + temp1 + temp2
            if temp_sum == value:
                ans.append([temp, temp1, temp2])
            return temp_sum

    # return helper(len(array)-1)
    # return divide_and_conquer(0, len(array)-1)
    sum_pairs(len(array)-1)
    return ans

print(find_largest())