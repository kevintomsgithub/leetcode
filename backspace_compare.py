def backspaceCompare(self, S: str, T: str) -> bool:
    def reducer(word):
        result = []
        for c in word:
            if c == '#':
                if len(result) > 0:
                    result.pop()
            else:
                result.append(c)
        return ''.join(result)
        
    s = reducer(S)
    t = reducer(T)
    return s == t