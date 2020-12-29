def myAtoi(s):
    s = s.strip()
    num = '0'
    sign = 0
    neg_flag = False
    for i in s:
        if i == '-' or i == '+':
            if sign != 0:
                break 
            neg_flag = True if i == '-' else False
            sign = 1
        elif i.isdigit(): num += i
        elif not i.isdigit(): 
            break
    num = int(num)
    if num > 2**31: 
        if neg_flag: return -2**31
        else: 2**31-1
    return -1*num if neg_flag else num

# a = "4193 with words"
# a = "   -42"
# a = "words and 987"
# a = "-91283472332"
# a = "3.14159"
# a = "+1"
# a = "  -0012a42"
# a = "+-2"
a = "-91283472332"
print(myAtoi(a))