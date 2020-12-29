def isAnagram(s, t):
    if len(s) != len(t): return False
    maps = {}
    for i in s:
        if i in maps: maps[i] += 1
        elif i not in maps: maps[i] = 1
    for j in t:
        if j in maps: maps[j] -= 1
        elif j not in maps: maps[j] = 1
    for i, j in maps.items():
        if j !=0:
            return False
    return True

s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car"
print(isAnagram(s, t))