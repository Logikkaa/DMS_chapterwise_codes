from collections import deque

def bfs_spanning_tree(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    spanning_tree = [[] for _ in range(n)]
    queue = deque([0])
    visited[0] = True

    while queue:
        node = queue.popleft()
        for neighbor in range(n):
            if adj_matrix[node][neighbor] and not visited[neighbor]:
                spanning_tree[node].append(neighbor)
                spanning_tree[neighbor].append(node)
                queue.append(neighbor)
                visited[neighbor] = True

    return spanning_tree

# Example usage
spanning_tree = bfs_spanning_tree(adj_matrix)
print(spanning_tree)
