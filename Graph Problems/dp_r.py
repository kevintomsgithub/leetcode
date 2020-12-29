def find_possible_subsets(array, total, i, mem):
    key = str([total, i])
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < array[i]:
        value = find_possible_subsets(array, total, i-1, mem)
    else:
        value = (find_possible_subsets(array, total - array[i], i-1, mem) +
                     find_possible_subsets(array, total, i-1, mem))
    mem[key] = value
    return value

def count_sets_dp(arr, total):
    mem = {}
    return find_possible_subsets(arr, total, len(arr)-1, mem)

n = 200
x = count_sets_dp([i for i in range(1, n) ], n)
print(x)