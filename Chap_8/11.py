import networkx as nx
import random

def generate_random_simple_graphs(num_graphs, num_vertices):
    graphs = []
    for _ in range(num_graphs):
        G = nx.Graph()
        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):
                if random.choice([True, False]):
                    G.add_edge(u, v)
        graphs.append(G)
    return graphs

def chromatic_number(G):
    return nx.coloring.greedy_color(G, strategy="largest_first")

num_graphs = 10
num_vertices = 20
graphs = generate_random_simple_graphs(num_graphs, num_vertices)
for i, G in enumerate(graphs):
    print(f"Graph {i+1}: Chromatic Number = {chromatic_number(G)}")
