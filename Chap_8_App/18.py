class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1

def kruskal_minimum_spanning_tree(graph):
    n = len(graph)
    edges = []
    for u in range(n):
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()

    mst = []
    ds = DisjointSet(n)
    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst

# Example usage
graph = [
    [(1, 2), (2, 3)],
    [(0, 2), (2, 4), (3, 1)],
    [(0, 3), (1, 4)],
    [(1, 1)]
]
mst = kruskal_minimum_spanning_tree(graph)
print(mst)
