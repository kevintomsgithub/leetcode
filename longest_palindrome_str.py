def longestPalindrome(s):
    if len(s) == 1: return s
    if len(s) == 2:
        if s[0] != s[1]:
            return s
        else:
            return ''
    length = max_len = 0
    long_pal_string = ''
    for i in range(1, len(s)-1):
        length = 0
        pal_str = s[i]
        j = k = i
        if s[i] == s[i+1]:
            pal_str = s[i] + s[i+1]
            length += 1
        elif s[i-1] == s[i]:
            pal_str = s[i-1] + s[i]
            length += 1
        while j>0 and k<len(s):
            j -= 1
            k += 1
            if s[j] == s[k]:
                pal_str = s[j]  + pal_str
                pal_str += s[k]
                length +=1
            else: break
        length = (length*2) + 1
        if max_len < length:
            max_len = length
            long_pal_string = pal_str
    return max_len, long_pal_string

def lp_seq(s):
    if len(s) == 0: return ''
    if len(s) == 1: return s
    if len(s) == 2:
        if s[0] == s[1]: return s
        else: return s[0]
    if len(set(s)) == 1: return s[0]
    longest_seq = s[0]
    for k in range(1, len(s)-1):
        i = k-1; j = k+1
        if s[i] == s[k]:
            curr_seq = s[i:k+1]
            if len(curr_seq) > len(longest_seq): longest_seq = curr_seq
        elif s[j] == s[k]:
            curr_seq = s[k:j+1]
            if len(curr_seq) > len(longest_seq): longest_seq = curr_seq
        while i>=0 and j<=len(s)-1:
            if s[i] == s[j]:
                curr_seq = s[i:j+1]
                if len(curr_seq) > len(longest_seq): longest_seq = curr_seq
                i -= 1; j += 1
            else: break
    return longest_seq


def lp(s):
    if len(s) == 0: return ''
    if len(s) == 1: return s
    if len(s) == 2:
        if s[0] == s[1]: return s
        else: return ''
    longest_seq = ''
    longest_seq_len = 0
    for k in range(1, len(s)-1):
        i = k-1; j = k+1
        # print(f'i: {i}, j: {j}')
        if s[i] == s[k]:
            curr_seq = s[i:k+1]
            if len(curr_seq) > len(longest_seq):
                longest_seq = curr_seq
                longest_seq_len = k-i+1
        elif s[j] == s[k]:
            curr_seq = s[k:j+1]
            if len(curr_seq) > len(longest_seq):
                longest_seq = curr_seq
                longest_seq_len = k-i+1
        while i>=0 and j<=len(s)-1:
            print(f's[{i}]: {s[i]}, s[{j}]: {s[j]}')
            if s[i] == s[j]:
                curr_len = j-i+1
                print(f'curr_len: {curr_len}')
                curr_seq = s[i:j+1]
                print(f'curr_seq: {curr_seq}')
                if len(curr_seq) > len(longest_seq):
                    longest_seq = curr_seq
                    longest_seq_len = curr_len
                    print('---Longer seq found: ', longest_seq)
                i -= 1; j += 1
            else:
                break
    return longest_seq, longest_seq_len


def longest_palindrome(s):
    if len(s) == 0: return ''
    start = 0; end = 0
    for i in range(len(s)):
        len_1 = expand_from_middle(s, i, i)
        len_2 = expand_from_middle(s, i, i+1)
        max_len = max(len_1, len_2)
        if max_len > end - start:
            start, end = i - (max_len-1)//2, i + (max_len//2)
    return s[start:end+1]

def expand_from_middle(s, left, right):
    while left>=0 and right<len(s) and s[left] == s[right]:
        left -= 1; right += 1
    return right - left - 1

a = 'aaa'
# print(longestPalindrome(a))
print(longest_palindrome(a))