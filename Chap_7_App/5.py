def connected_components(edges, n):
    graph = [[] for _ in range(n)]
    
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
        
    visited = [False] * n
    components = 0
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            components += 1
            dfs(i)
            
    return components

# Example input: List of vertex pairs
edges = [(1, 2), (2, 3), (4, 5)]
n = 5
result = connected_components(edges, n)
print("Number of Connected Components:", result)
