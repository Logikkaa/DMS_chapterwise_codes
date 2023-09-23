def is_bipartite(edges, n):
    color = [-1] * (n + 1)
    
    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
            if color[neighbor] == -1 and not dfs(neighbor, 1 - c):
                return False
        return True
    
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    for i in range(1, n + 1):
        if color[i] == -1 and not dfs(i, 0):
            return False
            
    return True

# Example input: List of edges
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
n = 4
result = is_bipartite(edges, n)
print("Is Bipartite:", result)
