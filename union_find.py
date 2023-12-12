def find(x):
    res = x
    while res != parent[x]:
        parent[res] = parent[parent[res]] # optimization
        res = parent[res]
    return res


def union(x, y):
    p1, p2 = find(x), find(y)
    if p1 == p2:
        return 0
    if rank[p2] > rank[p2]:
        parent[p1] = p2
        rank[p2] += rank[p1]
    else:
        parent[p2] = p1
        rank[p1] += rank[p1]
    return 1


n = 5
paths = [[0, 1], [1, 2], [3, 4]]

parent = list(range(n))
rank = [1] * n

res = n
for p in paths:
    res -= union(*p)

print(f"Connected components: {res}")


# ------------------------------------------------------


# Union Find
# parent = list(range(len(isConnected)))

# def find(x):
#     if x == parent[x]:
#         return x
#     return find(parent[x])

# def union(x, y):
#     parent[find(y)] = find(x)

# for x in range(len(isConnected)):
#     for y in range(len(isConnected)):
#         if isConnected[x][y] == 1:
#             union(x, y)

# province = [find(x) for x in parent]
# return len(set(province))
