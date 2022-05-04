def checkPalindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def countSubstrings_old(s):
        
    def helper(i, ss):
        if i == len(s):
            print(ss, len(ss))
            return checkPalindrome(ss) if len(ss) > 0 else 0
        return helper(i+1, ss+s[i]) + helper(i+1, ss)

    return helper(0, '')


def count_palindrome_from_center(s, i, j):
    result = 0

    while i>=0 and j<len(s):
        if s[i] != s[j]:
            break
        i -= 1
        j += 1
        result += 1

    return result

def countSubstrings(s):
    total = 0

    for i in range(len(s)):
        total += count_palindrome_from_center(s, i, i)
        total += count_palindrome_from_center(s, i, i+1)
    
    return total

s = 'abc'

# print(checkPalindrome(s))
print(countSubstrings(s))