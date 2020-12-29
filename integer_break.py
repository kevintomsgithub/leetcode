def integer_break_down(n):
    array = [i for i in range(1, n)]
    def helper(i, total, mem={}):
        # checks if in memory
        if str([i, total]) in mem: return mem[str([i, total])]
        # returns 0 for invalid cases
        if i < 0 or total < 0: return 0
        # returns 1 for valid cases
        if total == 0: return 1
        # takes the current element and the return of left subtree
        left = array[i] * helper(i, total-array[i])
        # takes return of right subtree
        right = helper(i-1, total)
        # takes the maximum value amoung left and right
        mem[str([i, total])] = max(left, right)
        return mem[str([i, total])]
    return helper(n-2, n)


def test(a=[0]):
    if len(a) == 10: return
    a.append(a[-1]+1)
    test(a)
    return a

print(integer_break_down(10))