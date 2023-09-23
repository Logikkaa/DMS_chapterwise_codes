def degree_of_each_vertex(edges):
    vertex_degree = {}
    
    for u, v in edges:
        if u not in vertex_degree:
            vertex_degree[u] = 0
        if v not in vertex_degree:
            vertex_degree[v] = 0
        vertex_degree[u] += 1
        vertex_degree[v] += 1
        
    return vertex_degree

# Example input: List of vertex pairs
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
result = degree_of_each_vertex(edges)
print(result)
