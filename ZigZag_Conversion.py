def convert(s, numRows):
    if numRows == 1: return s
    final_str = ''
    d = (numRows*2) - 2
    for i in range(numRows):
        row_str = ''
        if i == 0 or i == numRows-1:
            row_str = ''.join([s[k] for k in range(i, len(s), d)])
        else:
            for k in range(i, len(s), d):
                k_next_index = k+d-(2*i)
                row_str += s[k]+s[k_next_index] if k_next_index < len(s) else s[k]
        final_str += row_str
        print(row_str)
    return final_str

print(convert('PAYPALISHIRING', 4))