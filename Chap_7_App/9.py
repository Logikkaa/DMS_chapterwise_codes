import random

def generate_random_directed_graph(n):
    graph = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            graph[i][j] = random.choice([0, 1])
            
    return graph

# Example input: Number of vertices
n = 5
adjacency_matrix = generate_random_directed_graph(n)
for row in adjacency_matrix:
    print(row)
