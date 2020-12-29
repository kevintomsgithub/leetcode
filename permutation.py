
permutaions = []
def per(arr, temp_set=[], answers=[]):
    if len(arr) == 0:
        permutaions.append(list(temp_set))
    for i in range(len(arr)):
        temp = [arr[j] for j in range(len(arr)) if j!=i]
        temp_set.append(arr[i])
        per(temp, temp_set, answers)
        temp_set.pop()
    return answers

def permutaions_new(lst):
    if len(lst) == 0: return []
    elif len(lst) == 1: return [lst]
    else:
        subset = []
        for i in range(len(lst)):
            curr = lst[i]
            excluding = lst[:i] + lst[i+1:]
            for j in permutaions_new(excluding):
                subset.append( [curr] + j )
        return subset

array = [1,2,3]
# print(per(array))
print(permutaions_new(array))