class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False


def kruskal(nodes, edges):
    uf = UnionFind(nodes)
    mst = []

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))

    return mst


# Example graph with multiple MSTs
nodes = ['a', 'b', 'c', 'd']
edges = [
    (1, 'a', 'b'),
    (1, 'a', 'c'),  # same weight as (a, b)
    (1, 'b', 'c'),  # same weight again, allows tie
    (2, 'b', 'd'),
    (2, 'c', 'd')
]

# Sorting edges to prefer a specific MST
# Let's say we want the MST: ('a', 'b'), ('b', 'c'), ('b', 'd')
# We enforce this by sorting in that order despite same weights
preferred_order = [
    (1, 'a', 'b'),
    (1, 'b', 'c'),
    (1, 'a', 'c'),
    (2, 'b', 'd'),
    (2, 'c', 'd')
]

# Run Kruskal with preferred edge order
mst = kruskal(nodes, preferred_order)

# Output the result
print("MST returned by Kruskal's Algorithm:")
for u, v, w in mst:
    print(f"{u} - {v} (weight {w})")
