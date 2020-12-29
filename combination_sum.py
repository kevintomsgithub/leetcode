def combinationSum(candidates, target):
    if len(candidates) == 0: return []
    results = []
    def helper(i, total, subarray=[], mem={}):
        if total == 0 and subarray not in results:
            results.append(subarray)
            return subarray
        elif i < 0 or total < 0: return []
        elif candidates[i] > total:
            helper(i-1, total, subarray)
        else:
            helper(i, total-candidates[i], subarray+[candidates[i]], mem)
            helper(i-1, total, subarray, mem)
    helper(len(candidates)-1, target)
    return results

array = [2, 3, 5]
target = 8
print(combinationSum(array, target))