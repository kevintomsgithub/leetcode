def BFS(root):
    q = [root]; v = [root]
    while q:
        r = q.pop(0)
        path.append(r)
        for n in graph[r]:
            if n not in v:
                v.append(n)
                q.append(n)

def DFS(root):
    q = [root]; v = [root]
    while q:
        r = q.pop()
        path.append(r)
        for n in graph[r]:
            if n not in v:
                v.append(n)
                q.append(n)


def dfs_rec(root):
    path.append(root)
    for r in graph[root]:
        dfs_rec(r)
    
def bfs_rec(q, v):
    if not q: return
    r = q.pop()
    for n in graph[r]:
        if n not in v:
            v.append(n)
            path.append(n)
            q.append(n)
    return bfs_rec(q, v)

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [9],
    6: [10],
    7: [11],
    8: [],
    9: [],
    10: [],
    11: [],
}
path = []
root = 1
# BFS(root)
# DFS(root)
# dfs_rec(root)
bfs_rec([1], [1])
print(path)