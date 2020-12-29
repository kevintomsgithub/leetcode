def find_shortest_path(start):
    queue = [start]
    visited = [start]
    distance = {start: 0}
    def add_node_properties(n, c):
        if n in distance:
            distance[n] += 1
        else:
            distance[n] = distance[c] + 1
        queue.append(n)
        visited.append(n)
        # print('Visited: ', visited)
        # print('Distance: ', distance)
    while queue:
        print('Queue: ', queue)
        node = queue.pop(0)
        if 1 in distance:
            return distance[1]
        if node%2 == 0:
            new_node = node//2
            if new_node not in visited:
                add_node_properties(new_node, node)
        else:
            ln = node-1
            rn = node+1
            if ln not in visited:
                add_node_properties(ln, node)
            if rn not in visited:
                add_node_properties(rn, node)
        print('Distance: ', distance)


def solution(n):
    n = int(n)
    queue = [n]
    visited = [n]
    distance = {n: 0}
    def add_node(new_node, current_node):
        if new_node in distance:
            distance[new_node] += 1
        else:
            distance[new_node] = distance[current_node] + 1
        queue.append(new_node)
        visited.append(new_node)
    while queue:
        node = queue.pop(0)
        if 1 in distance:
            return distance[1]
        if node%2 == 0:
            new_node = node//2
            if new_node not in visited:
                add_node(new_node, node)
        else:
            ln = node - 1
            rn = node + 1
            if ln not in visited:
                add_node(ln, node)
            if rn not in visited:
                add_node(rn, node)

x = solution('15')
print('Shortest path: ', x)
