
class Node:
    
    def __init__(self, val, neighbours=None) -> None:
        self.val = val
        self.neighbours = [] if neighbours is None else neighbours
        

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3],
}


def bfs(node):
    
    q = [node]
    v = [node]
    
    while q:
        n = q.pop(0)
        for i in graph[n]:
            if i not in v:
                v.append(i)
                q.append(i)
    
    return v

def dfs(node):
    
    s = [node]
    v = [node]
    
    while s:
        n = s.pop()
        for i in graph[n]:
            if i not in v:
                v.append(i)
                s.append(i)
    
    return v


def dfs_rec(node):
    
    if node == None:
        return None
    
    v.append(node)
    
    if node not in v:
        for n in graph[node]:
            dfs_rec(n)
    
    


v = []

# print(bfs(1))

# print(dfs(1))

dfs_rec(1)

print(v)