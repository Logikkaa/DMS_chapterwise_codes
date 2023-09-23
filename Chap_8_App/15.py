def is_safe(vertex, color, graph, colored):
    for neighbor in graph[vertex]:
        if colored[neighbor] == color:
            return False
    return True

def color_graph_backtracking(graph, colors, vertex=0, colored=None):
    if colored is None:
        colored = [-1] * len(graph)

    if vertex == len(graph):
        return colored

    for color in colors:
        if is_safe(vertex, color, graph, colored):
            colored[vertex] = color
            if color_graph_backtracking(graph, colors, vertex + 1, colored):
                return colored
            colored[vertex] = -1

    return None

# Example usage
graph = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]
colors = [0, 1, 2]
colored = color_graph_backtracking(graph, colors)
print(colored)
