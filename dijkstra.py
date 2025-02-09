import heapq


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, src, dst, weight):
        self.adj_list[src].append((dst, weight))

    def dijkstra(self, src):
        dist = {}
        min_heap = [(0, src)]
        previous_node = {i: None for i in range(self.V)}
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in dist:
                continue
            dist[n1] = w1
            for n2, w2 in self.adj_list[n1]:
                if n2 not in dist:
                    heapq.heappush(min_heap, [w1 + w2, n2])
                    previous_node[n2] = n1
        return dist, previous_node

    def get_shortest_path(self, previous_node, target):
        path = []
        while target:
            path.insert(0, target)
            target = previous_node[target]
        return path


g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(2, 1, 4)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 5)

dist, previous_node = g.dijkstra(0)
print(f"distance: {dist}")
path = g.get_shortest_path(previous_node, 3)
print(f"path: {path}")
