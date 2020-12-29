def rec(arr, i):
    s_s = ''
    s_rep = '0'
    n_s_s = ''
    while i < len(arr):
        if arr[i].isdigit():
            s_rep += arr[i]
        elif arr[i].isalpha():
            s_s += arr[i]
        elif arr[i] == '[':
            n_rep = int(s_rep)
            s_rep = '0'
            n_s_s, i = rec(arr, i+1)
            s_s += n_s_s if n_rep == 0 else n_rep * n_s_s
        elif arr[i] == ']':
            return s_s, i
        i += 1

    if s_rep == '0':
        return s_s
    return int(s_rep) * n_s_s

x = rec('a0[c]b', 0)
print(x)