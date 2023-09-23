def construct_euler_path_circuit(edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
    
    indegrees = defaultdict(int)
    outdegrees = defaultdict(int)
    
    for u, v in edges:
        outdegrees[u] += 1
        indegrees[v] += 1
    
    start = None
    end = None
    
    for node in indegrees:
        if indegrees[node] > outdegrees[node]:
            end = node
        elif indegrees[node] < outdegrees[node]:
            start = node
    
    if start is None and end is None:
        start = edges[0][0]
        end = edges[0][1]
    
    def dfs(node, path):
        while graph[node]:
            neighbor = graph[node].pop(0)
            dfs(neighbor, path)
        path.append(node)
    
    path = []
    dfs(start, path)
    return path

# Example input: List of directed vertex pairs
edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
result = construct_euler_path_circuit(edges)
print("Euler Path or Circuit:", result)
