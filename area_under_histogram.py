def find_max_area(n):
    stack = []; i=0; max_area = -1
    while i < len(n):
        if stack == []:
            stack.append(i)
            i += 1
        else:
            if n[stack[-1]] < n[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if stack: area = n[top]*(i-stack[-1]-1)
                else: area = n[top] * i
                if max_area < area: max_area = area
    return max_area

a = [-2, -1, -2, -3]
print(find_max_area(a+[0]))