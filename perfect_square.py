def numSquares_get_pairs(n):
    def helper(a, i, total, subarray=[], mem={}):
        if total == 0: return subarray
        if total < 0 or i < 0: return -1
        if str([i, total]) in mem: 
            return mem[str([i, total])]
        left = helper(a, i, total-a[i], subarray+[a[i]])
        right = helper(a, i-1, total, subarray)
        if left != -1 and right != -1:
            to_return = left if len(left) < len(right) else right
        else: 
            to_return = right if left == -1 else left
        mem[str([i, total])] = to_return
        return to_return

    a = [i*i for i in range(1, (int(n**(1/2))+1))]
    subset = helper(a, len(a)-1, n)
    return [subset, len(subset)]


def numSquares(n):
    def helper(a, i, total, mem={}):
        if total == 0: return 0
        elif total < 0 or i < 0: return -1
        elif str([i, total]) in mem: 
            return mem[str([i, total])]
        elif a[i] > total: 
            return helper(a, i-1, total)
        else:
            left = 1 + helper(a, i, total-a[i])
            right = helper(a, i-1, total)
        if left != -1 and right != -1:
            to_return = min(left, right)
        else:
            to_return = max(left, right)
        mem[str([i, total])] = to_return
        return to_return

    a = [i*i for i in range(1, (int(n**(1/2))+1))]
    return helper(a, len(a)-1, n)

n = 7217
print(numSquares_get_pairs(n))
print(numSquares(n))