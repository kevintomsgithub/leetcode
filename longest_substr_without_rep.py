def longest_substring(s):
    if len(s) == 0: return ''
    longest_length = 0
    l_str = ''
    prev_chars = []
    i = start = 0
    while i < len(s):
        if s[i] not in prev_chars:
            prev_chars.append(s[i])
        else:
            if longest_length < len(prev_chars):
                longest_length = len(prev_chars)
                l_str = ''.join(prev_chars)
            prev_chars = []
            i = start
            start += 1
        i += 1
    if longest_length < len(prev_chars):
        longest_length = len(prev_chars)
        l_str = ''.join(prev_chars)
    return [l_str, longest_length]


def lengthOfLongestSubstring(s):
    dicts = {}
    maxlength = start = 0
    for i,value in enumerate(s):
        if value in dicts:
            sums = dicts[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxlength:
            maxlength = num
        dicts[value] = i
    return maxlength


def longestSubstring(s):
    mapping = {}
    max_len = start = 0
    for index, letter in enumerate(s):
        if letter in mapping:
            new_start = mapping[letter] + 1
            if new_start > start:
                start = new_start
        length = index - start + 1
        if length > max_len:
            max_len = length
        mapping[letter] = index
    return max_len


s = "abcdaqfg"
print(longestSubstring(s))

