def strStr(haystack, needle):
    if len(needle) == 0: return 0
    if len(needle) > len(haystack): return -1
    for i in range(len(haystack)-(len(needle) - 1)):
        j=0
        while j < len(needle):
            if haystack[i+j] != needle[j]: break
            j += 1
        if j == len(needle): return i
    return -1

h = "a"
n = "a"
# h = "mississippi"
# n = "issipi"
print(strStr(h, n))