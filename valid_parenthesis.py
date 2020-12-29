def validate_parentheses(s):
    if len(s) == 0:
        return True
    stack = []
    i = 0
    while i<len(s):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        else:
            if len(stack) == 0: return False
            b = stack.pop()
            if s[i] == ')':
                if b != '(':
                    return False
            if s[i] == ']':
                if b != '[':
                    return False
            if s[i] == '}':
                if b != '{':
                    return False
        i += 1
    return len(stack) == 0

exp = "([{}])"
print(validate_parentheses(exp))