from collections import defaultdict

class DFSTopologicalSort:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0
        self.discovery = {}
        self.finishing = {}
        self.visited = set()
        self.edge_classification = []
        self.topo_stack = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self):
        for node in sorted(self.graph):  # Process vertices in alphabetical order
            if node not in self.visited:
                self._dfs_visit(node)

    def _dfs_visit(self, u):
        self.time += 1
        self.discovery[u] = self.time
        self.visited.add(u)

        for v in sorted(self.graph[u]):  # Alphabetical neighbor ordering
            if v not in self.discovery:
                self.edge_classification.append((u, v, "Tree"))
                self._dfs_visit(v)
            elif v not in self.finishing:
                self.edge_classification.append((u, v, "Back"))
            elif self.discovery[u] < self.discovery[v]:
                self.edge_classification.append((u, v, "Forward"))
            else:
                self.edge_classification.append((u, v, "Cross"))

        self.time += 1
        self.finishing[u] = self.time
        self.topo_stack.append(u)

    def get_topological_sort(self):
        return list(reversed(self.topo_stack))

    def get_times(self):
        return self.discovery, self.finishing

    def get_edge_classifications(self):
        return self.edge_classification


# Example usage with Figure 22.8
dag = DFSTopologicalSort()

# Add edges from the graph
edges = [
    ('m', 'n'), ('m', 'q'),
    ('n', 'o'), ('n', 'u'),
    ('o', 'r'), ('o', 's'),
    ('p', 'o'), ('p', 's'),
    ('q', 'r'), ('q', 't'), ('q', 'u'),
    ('r', 'v'), ('s', 'v'),
    ('t', 'x'), ('u', 'x'), ('u', 'y'),
    ('v', 'y'), ('v', 'w'),
    ('w', 'z')
]

for u, v in edges:
    dag.add_edge(u, v)

# Run DFS
dag.dfs()

# Output
print("Topological Sort Order:")
print(dag.get_topological_sort())

print("\nDiscovery Times:")
for k, v in dag.get_times()[0].items():
    print(f"{k}: {v}")

print("\nFinishing Times:")
for k, v in dag.get_times()[1].items():
  print(f"{k}: {v}")

print("\nEdge Classifications:")
for u, v, edge_type in dag.get_edge_classifications():
    print(f"{u} -> {v}: {edge_type}")
