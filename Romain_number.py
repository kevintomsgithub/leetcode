def get_number(R):
    R_val = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    R += 'e'
    total = 0
    i = 0
    while i < len(R)-1:
        if R[i+1] == 'e':
            total += R_val[R[i]]
            return total
        curr = R_val[R[i]]
        post = R_val[R[i+1]]
        if curr < post:
            sub = post-curr
            total += sub
            i += 1
        else:
            total += curr
        i += 1
    return total

x = get_number('MCMXCIV')
print(x)