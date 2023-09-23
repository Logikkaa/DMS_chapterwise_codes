def in_out_degree(edges):
    in_degree = {}
    out_degree = {}
    
    for u, v in edges:
        if u not in in_degree:
            in_degree[u] = 0
        if v not in out_degree:
            out_degree[v] = 0
        in_degree[v] = in_degree.get(v, 0) + 1
        out_degree[u] = out_degree.get(u, 0) + 1
        
    return in_degree, out_degree

# Example input: List of directed edges
edges = [(1, 2), (2, 3), (1, 3), (3, 1)]
in_degrees, out_degrees = in_out_degree(edges)
print("In-degrees:", in_degrees)
print("Out-degrees:", out_degrees)
