def knapsack():
    w = [10, 5, 7, 2]
    v = [1, 2, 3, 4]
    capacity = 17
    ans = []
    def helper(n, C):
        if n == -1 or C == 0:
            return 0
        elif w[n] > C:
            return helper(n-1, C)
        else:
            v1 = v[n] + helper(n-1, C-w[n])
            v2 = helper(n-1, C)
            print(f'n: {w[n]}, C: {C}, temp1: {v1}, temp2: {v2}')
            return max(v1, v2)

    def helper_pair(n, C, array):
        if C == 0:
            ans.append(array)
            print('-----Answers: ', array)
        if n == -1:
            return 0
        elif w[n] > C:
            return helper_pair(n-1, C, array)
        else:
            array.append(w[n])
            v1 = v[n] + helper_pair(n-1, C-w[n], array)
            array.pop()
            v2 = helper_pair(n-1, C, array)
            return max(v1, v2)

    def helper_anton(n, C):
        max_val = 0
        for i in range(n, len(w)):
            if w[i] <= C:
                temp_val = helper_anton(i+1, C-w[i])
                temp_max = temp_val + v[i]
                if temp_max > max_val:
                    max_val = temp_max
        return max_val
    
    # result = helper(len(w)-1, capacity)
    result = helper_pair(len(w)-1, capacity, [])
    # result = helper_anton(0, capacity)
    return result, ans

print(knapsack())