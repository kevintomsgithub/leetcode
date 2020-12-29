class TopologicalSort:
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['H', 'F'],
        'F': ['G'],
        'G': [],
        'H': [],    
    }
    nodes = list(graph.keys())
    v = []; q = []; path = []; stack = []

    def topological_sort(self):
        for node in self.nodes:
            if node not in self.v:
                self.traverse(node)
        return self.stack[::-1]

    def traverse(self, node):
        self.v.append(node)
        for n in self.graph[node]:
            if n not in self.v:
                self.traverse(n)
        self.stack.append(node)

x = TopologicalSort().topological_sort()
print(x)