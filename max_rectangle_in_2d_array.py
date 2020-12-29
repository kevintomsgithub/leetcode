def find_area_under_histogram(n):
    stack = []; i = 0; max_area = -1
    while i<len(n):
        if stack == []:
            stack.append(i)
            i += 1
        else:
            if n[i] > n[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if stack: area = n[top]*(i-stack[-1]-1)
                else: area = n[top]*i
                if max_area < area : max_area = area
    return max_area

def find_max_rectangle(n):
    if len(n) == 0: return 0
    rows, cols = len(n), len(n[0])
    hist = [0 for i in range(cols)]; max_area = -1
    for i in range(rows):
        for j in range(cols):
            if int(n[i][j]) != 0: hist[j] += int(n[i][j])
            else: hist[j] = 0
        area = find_area_under_histogram(hist+[0])
        if area > max_area : max_area = area
    return max_area

# array = [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
array = [
    ["0","1"],
    ["1","0"]
]
print(find_max_rectangle(array))