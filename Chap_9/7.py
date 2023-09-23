import networkx as nx

# Example distances between cities
distances = {
    ('A', 'B'): 100,
    ('A', 'C'): 150,
    ('B', 'C'): 200,
    # Add more distances
}

G = nx.Graph()

for cities, distance in distances.items():
    G.add_edge(cities[0], cities[1], weight=distance)

# Find minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Print edges and their weights in the minimum spanning tree
for edge in mst.edges(data=True):
    print(edge)
