def reverse_old(x):
    neg_flag = True if x < 0 else False
    if neg_flag: s = list(str(x)[1:])
    else: s = list(str(x))
    i=0; j=len(s)-1
    for i in range(len(s)//2):
        s[i], s[j-i] = s[j-i], s[i]
    if neg_flag:
        return -1 * int(''.join(s))
    return int(''.join(s))

def reverse(x):
    neg_flag = False
    if x < 0:
        neg_flag = True
        x *= -1
    rev = 0
    while x > 0:
        pop = x % 10
        rev = (rev * 10) + pop
        x //= 10
    print(2**32)
    if rev > 2**31: return 0
    return -1*rev if neg_flag else rev

print(reverse(1563847412))