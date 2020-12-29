def countNumbersWithUniqueDigits(n):
    if n == 0: return 1
    if n == 1: return 10
    array = [1, 10]; c = 9
    while n > 1:
        array.append((array[-1]-array[-2])*c + array[-1])
        n -= 1; c -= 1
    return array[-1]
    
print(countNumbersWithUniqueDigits(3))