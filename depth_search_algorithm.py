from collections import defaultdict

class DFSWithClassification:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0
        self.discovery = {}
        self.finishing = {}
        self.visited = set()
        self.edge_types = []
        self.result = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self):
        # Visit all vertices in alphabetical order
        for node in sorted(self.graph):
            if node not in self.visited:
                self._dfs_visit(node)

    def _dfs_visit(self, u):
        self.time += 1
        self.discovery[u] = self.time
        self.visited.add(u)

        # Visit neighbors in alphabetical order
        for v in sorted(self.graph[u]):
            if v not in self.discovery:
                self.edge_types.append((u, v, "Tree"))
                self._dfs_visit(v)
            elif v not in self.finishing:
                self.edge_types.append((u, v, "Back"))
            elif self.discovery[u] < self.discovery[v]:
                self.edge_types.append((u, v, "Forward"))
            else:
                self.edge_types.append((u, v, "Cross"))

        self.time += 1
        self.finishing[u] = self.time
        self.result.append(u)

    def get_discovery_finishing_times(self):
        return self.discovery, self.finishing

    def get_edge_classifications(self):
        return self.edge_types

    def get_dfs_finish_order(self):
        return list(reversed(self.result))


# --- Graph from Figure 22.6 ---
dfs_graph = DFSWithClassification()
edges = [
    ('q', 's'), ('q', 't'),
    ('r', 'u'),
    ('s', 'v'),
    ('t', 'x'),
    ('u', 'y'),
    ('v', 'w'),
    ('w', 's'),
    ('x', 'y'),
    ('y', 'q'),
    ('z', 'x'), ('z', 'z')  # self-loop
]

for u, v in edges:
    dfs_graph.add_edge(u, v)

# Run DFS
dfs_graph.dfs()

# Display Results
print(" DFS Finish Order (Topological Postorder):")
print(dfs_graph.get_dfs_finish_order())

print("\n🕒 Discovery and Finishing Times:")
discovery, finishing = dfs_graph.get_discovery_finishing_times()
for node in sorted(discovery, key=discovery.get):
   print(f"{node}: d = {discovery[node]}, f = {finishing[node]}")

print("\n🔗 Edge Classifications:")
for u, v, t in dfs_graph.get_edge_classifications():
    print(f"{u} -> {v}: {t}")
