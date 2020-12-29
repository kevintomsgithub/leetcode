def find_connections(graph, start, d):
    """Find connection nodes in range of 2"""
    q = [start]
    v = [start]
    nodes_in_distance = []
    depth = 1
    while q:
        s = q.pop(0)
        for i in graph[s]:
            if i not in v:
                if depth != d:
                    q.append(i)
                else:
                    nodes_in_distance.append(i)
                v.append(i)
        if depth != d:
            depth += 1
    return len(nodes_in_distance)

Graph = {}
v, e = map(int, input().split(' '))
for i in range(e):
    v1, v2 = map(int, input().split(' '))
    if v1 not in Graph:
        Graph[v1] = [v2]
    else:
        Graph[v1].append(v2)
    if v2 not in Graph:
        Graph[v2] = [v1]
    else:
        Graph[v2].append(v1)
./
queries = int(input())
queries_list = []
for i in range(queries):
    n, d = map(int, input().split(' '))
    queries_list.append([n, d])

for n, d in queries_list:
    print(find_connections(Graph, n, d))