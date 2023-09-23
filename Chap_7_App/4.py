def construct_adjacency_matrix(edges, n):
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    for u, v in edges:
        adjacency_matrix[u - 1][v - 1] = 1
        adjacency_matrix[v - 1][u - 1] = 1
        
    return adjacency_matrix

# Example input: List of vertex pairs
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
n = 4
result = construct_adjacency_matrix(edges, n)
for row in result:
    print(row)
