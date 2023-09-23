def hamilton_path(edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
    
    def dfs(node, path):
        if len(path) == n:
            return True
        for neighbor in graph[node]:
            if neighbor not in path:
                path.append(neighbor)
                if dfs(neighbor, path):
                    return True
                path.pop()
        return False
    
    n = len(graph)
    
    for node in graph:
        path = [node]
        if dfs(node, path):
            return path
        
    return []

# Example input: List of vertex pairs
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
result = hamilton_path(edges)
print("Hamilton Path:", result)
