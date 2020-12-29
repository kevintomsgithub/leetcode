def numDecodings(s):
    if len(s) == 0: return 0
    def dfs(string, mem={}):
        if len(string) >= 1 and string[0] == '0': return 0
        if len(string) <= 1: return 1
        if string in mem: return mem[string]
        first = dfs(string[1:], mem)
        second = dfs(string[2:], mem) if int(string[:2]) <= 26 else 0
        mem[string] = first + second
        return mem[string]
    return dfs(s)
        
print(numDecodings('223'))