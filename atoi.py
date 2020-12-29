def myAtoi(s):
    s = s.strip()
    if s == '': return 0
    if '-' in s and '+' in s: return 0
    if s[0] not in [str(i) for i in range(10)]+['-', '+']:
        return 0
    if '.' in s: s=s.split('.')[0]
    number = []
    neg_flag = False
    for i in s:
        if i == '-':
            neg_flag = True
        elif i.isdigit():
            number.append(i)
    if len(number)==0: return 0
    n = int(''.join(number))
    if n > 2**31:
        n = 2**31
    return -n if neg_flag else n

print(myAtoi('+'))