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
    
def solution(n):
    memory = {}
    array = [i for i in range(1, n)]
    return find_possible_subsets(array, n, len(array)-1, memory)

print(solution(10))