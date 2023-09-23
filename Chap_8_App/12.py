def dfs_spanning_tree(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    spanning_tree = [[] for _ in range(n)]

    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if adj_matrix[node][neighbor] and not visited[neighbor]:
                spanning_tree[node].append(neighbor)
                spanning_tree[neighbor].append(node)
                dfs(neighbor)

    dfs(0)
    return spanning_tree

# Example usage
adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
spanning_tree = dfs_spanning_tree(adj_matrix)
print(spanning_tree)
