import heapq

def dijkstra(edges, n, start, end):
    graph = defaultdict(list)
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                
    shortest_path = []
    node = end
    while node != start:
        shortest_path.append(node)
        for neighbor, weight in graph[node]:
            if distances[node] == distances[neighbor] + weight:
                node = neighbor
                break
                
    shortest_path.append(start)
    shortest_path.reverse()
    
    return distances[end], shortest_path

# Example input: List of directed edges with weights
edges = [(1, 2, 2), (1, 3, 4), (2, 3, 1), (2, 4, 7), (3, 4, 3)]
n = 4
start_node = 1
end_node = 4
distance, shortest_path = dijkstra(edges, n, start_node, end_node)
print("Shortest Distance:", distance)
print("Shortest Path:", shortest_path)
