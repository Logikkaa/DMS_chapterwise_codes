def is_tree(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True
        for neighbor in range(n):
            if adj_matrix[node][neighbor] and not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif adj_matrix[node][neighbor] and neighbor != parent:
                return True
        return False

    components = 0
    for node in range(n):
        if not visited[node]:
            components += 1
            if components > 1:
                return False
            if dfs(node, -1):
                return False

    return components == 1

# Example usage
adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
print(is_tree(adj_matrix))
