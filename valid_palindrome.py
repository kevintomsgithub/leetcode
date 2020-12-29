def isPalindrome(s):
    if len(s) == '': return True
    new_s = ''
    for letter in s.lower():
        if ord(letter) >= 97 and ord(letter) <= 122 or letter.isnumeric():
            new_s += letter
    print(new_s)
    j=len(new_s) - 1
    for i in range(len(new_s)//2):
        if new_s[i] != new_s[j-i]:
            return False
    return True

# a = "A man, a plan, a canal: Panama"
a = "0p"
print(isPalindrome(a)) 