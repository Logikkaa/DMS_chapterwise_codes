import heapq

def prim_minimum_spanning_tree(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    spanning_tree = [[] for _ in range(n)]

    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        if visited[vertex]:
            continue
        visited[vertex] = True
        for neighbor, edge_weight in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))
                spanning_tree[vertex].append((neighbor, edge_weight))
                spanning_tree[neighbor].append((vertex, edge_weight))

    return spanning_tree

# Example usage
graph = [
    [(1, 2), (2, 3)],
    [(0, 2), (2, 4), (3, 1)],
    [(0, 3), (1, 4)],
    [(1, 1)]
]
spanning_tree = prim_minimum_spanning_tree(graph)
print(spanning_tree)
