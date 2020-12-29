def letterCombinations(digits):
    '''
    2 - abc
    3 - def
    4 - ghi
    [a, b, c] [d, e, f] [g, h, i]
    result - ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    '''
    digit_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    result = []
    def generate_combinations(i=0, combination=''):
        if i == len(digits): 
            result.append(combination)
            return
        for letter in digit_map[digits[i]]:
            generate_combinations(i+1, combination+letter)
    generate_combinations()
    return result

n = ''
print(letterCombinations(n))