def count_paths(edges, n, start, end):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
    
    def dfs(node, length):
        if length == n:
            return 1 if node == end else 0
        count = 0
        for neighbor in graph[node]:
            count += dfs(neighbor, length + 1)
        return count
    
    return dfs(start, 0)

# Example input: List of vertex pairs, length n, start and end nodes
edges = [(1, 2), (2, 3), (3, 4), (1, 4)]
n = 3
start_node = 1
end_node = 4
result = count_paths(edges, n, start_node, end_node)
print("Number of Paths:", result)
