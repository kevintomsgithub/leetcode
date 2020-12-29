graph = {
    1: [2, 3],
    2: [4, 1],
    3: [5, 1],
    4: [2],
    5: [3],
}

def BFS(root):
    queue = [root]
    visited = [root]
    while queue:
        node = queue.pop(0)
        print(node)
        for i in graph[node]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

def DFS(root):
    stack = [root]
    visited = [root]
    while stack:
        node = stack.pop()
        print(node)
        for i in graph[node]:
            if i not in visited:
                stack.append(i)
                visited.append(i)

DFS(1)