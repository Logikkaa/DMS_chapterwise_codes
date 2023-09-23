def is_isomorphic(graph1, graph2):
    return sorted(graph1) == sorted(graph2)

# Example input: List of vertex pairs for two graphs
edges1 = [(1, 2), (2, 3), (3, 1)]
edges2 = [(2, 1), (1, 3), (3, 2)]
result = is_isomorphic(edges1, edges2)
print("Graphs are Isomorphic:", result)
