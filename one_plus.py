def plusOne(digits):
    carry = 1
    i = len(digits) - 1
    while carry==1 and i >= 0:
        carry = 1 if digits[i]+1 > 9 else 0
        digits[i] = 0 if carry == 1 else digits[i]+1
        i -= 1
    if carry==1:
        digits.insert(0, 1)
    return digits

d = [0]
print(plusOne(d))