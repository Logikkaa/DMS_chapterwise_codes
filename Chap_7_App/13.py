def euler_path_circuit(edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
    
    def dfs(node, path):
        while graph[node]:
            neighbor = graph[node].pop()
            dfs(neighbor, path)
        path.append(node)
        
    in_degrees = [0] * (n + 1)
    out_degrees = [0] * (n + 1)
    
    for u, v in edges:
        out_degrees[u] += 1
        in_degrees[v] += 1
    
    start_node = None
    end_node = None
    
    for i in range(1, n + 1):
        if out_degrees[i] > in_degrees[i]:
            start_node = i
        elif in_degrees[i] > out_degrees[i]:
            end_node = i
            
    if start_node is None and end_node is None:
        start_node = 1
    
    path = []
    dfs(start_node, path)
    path.reverse()
    
    if end_node:
        path.remove(start_node)
        path.append(end_node)
    
    return path

# Example input: List of vertex pairs
edges = [(1, 2), (1, 2), (2, 3), (3, 1), (3, 1)]
n = 3
result = euler_path_circuit(edges)
print("Euler Path or Circuit:", result)
