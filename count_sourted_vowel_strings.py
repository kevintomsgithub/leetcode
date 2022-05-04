def countVowelStrings_pairs(n):
    vowels = [c for c in 'aeiou']
    pairs = []

    def helper(i, j, pair=''):
        if i == 0:
            pairs.append(pair)
            return 1
        if j == len(vowels):
            pairs.append(pair)
            return 1
        count = 0
        for j in range(j, len(vowels)):
            count += helper(i-1, j, pair+vowels[j])
        return count
    
    result = helper(n, 0)
    print(pairs)
    return result

def countVowelStrings(n):
    vowels_len = 5
    def helper(i, j):
        if i == 0:
            return 1
        if j == vowels_len:
            return 1
        count = 0
        for j in range(j, vowels_len):
            count += helper(i-1, j)
        return count

    return helper(n, 0)

def countVowelStrings_mem(n):
    vowels = [c for c in 'aeiou']
    mem = {}
    def helper(i, j):
        if i == 0:
            return 1
        if j == len(vowels):
            return 1
        if (i, j) in mem:
            return mem[(i, j)]
        count = 0
        for j in range(j, len(vowels)):
            count += helper(i-1, j)
            print((i, vowels[j]), count)
        mem[(i, j)] = count
        return count

    return helper(n, 0)

n = 3
print(countVowelStrings(n))