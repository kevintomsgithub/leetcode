def isSubsequence(s, t):
    """
    time: O(max(s, t))
    space: O(1)
    """
    if len(s) == 0: return True
    s_ptr, t_ptr = 0, 0
    char_match = 0
    while t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            char_match += 1
            if char_match == len(s): return True
            s_ptr += 1
        t_ptr += 1
    return char_match == len(s)

def binary_search(c, s):

def isSubsequence_BinarySearch(s, t):
    """
    time: O(max(s, t))
    space: O(1)
    """
    if len(s) == 0: return True
    current_index = 0
    for c in s:
        current_index = binary_search(c, s[current_index:])

s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))