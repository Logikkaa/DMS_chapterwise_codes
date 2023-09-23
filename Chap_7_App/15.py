def hamilton_circuit(edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
    
    def dfs(node, path):
        if len(path) == n:
            if path[-1] in graph[path[0]]:
                path.append(path[0])
                return True
            return False
        for neighbor in graph[node]:
            if neighbor not in path:
                path.append(neighbor)
                if dfs(neighbor, path):
                    return True
                path.pop()
        return False
    
    n = len(graph)
    path = []
    
    for node in graph:
        path.append(node)
        if dfs(node, path):
            return path
        
        path.pop()
    
    return []

# Example input: List of vertex pairs
edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
result = hamilton_circuit(edges)
print("Hamilton Circuit:", result)
