def clone_graph(root):
    q = [root]; v = [root]
    while q:
        r = q.pop()
        clone[r] = graph[r]
        for n in graph[r]:
            if n not in v:
                v.append(n)
                q.append(n)

graph = {
    'A': ['C', 'B'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['C', 'B', 'E'],
    'E': ['D'],
}
clone = {}
root = 'A'
clone_graph(root)
print(clone)