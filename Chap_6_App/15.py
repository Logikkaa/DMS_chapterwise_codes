from collections import defaultdict, deque

def topological_sort(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque()
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)

    total_ordering = []
    while queue:
        node = queue.popleft()
        total_ordering.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return total_ordering

# Example usage
partial_order = {1: [2, 3], 2: [4], 3: [4], 4: []}
total_order = topological_sort(partial_order)
print("Total Ordering:", total_order)
