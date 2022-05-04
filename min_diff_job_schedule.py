import sys

def findMinComplexity(complexity, days):
    if days > len(complexity):
        return -1

    def helper_(i=0, mem={}):
        if i == len(s):
            return ['']
        if i in mem:
            return mem[i]
        result = []
        for j in range(i+1, len(s)+1):
            if s[i:j] in wordDict:
                for tail in helper(j):
                    result.append( s[i:j] + (' ' + tail if tail!= '' else ''))
        mem[i] = result
        return result

    def helper(d, i=0, mem={}):
        if d == 1:
            return complexity[i:]
        if (i, d) in mem:
            return mem[(i, d)]
        min_complexity = sys.maxsize
        for j in range(i, len(complexity)-(d-1)):
            min_complexity = min(min_complexity, max(complexity[i:j+1]) + max(helper(d-1, j+1, mem)))
        mem[(i, d)] = [min_complexity]
        return [min_complexity]
    return min(helper(days))

# jobDifficulty = [7,1,7,1,7,1]
# d = 3

# jobDifficulty = [9,9,9]
# d = 4

# jobDifficulty = [6,5,4,3,2,1]
# d = 2

# jobDifficulty = [30, 10, 40, 20, 50]
# d = 2

# jobDifficulty = [186,398,479,206,885,423,805,112,925,656,16,932,740,292,671,360]
# d = 4

jobDifficulty = [920,539,840,271,685,491,802,635,240,339,353,483,65,945,122,944,638,618,873,382,183,891,582,839,781,331,178,888,437,490,411,47,327,977,135,408,454,963]
d = 1

print(findMinComplexity(jobDifficulty, d))