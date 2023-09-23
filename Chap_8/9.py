import networkx as nx
import random

def generate_graph_with_euler_circuit(num_vertices):
    while True:
        G = nx.eulerian_circuit(nx.complete_graph(num_vertices))
        if G is not None:
            return G

num_vertices = 10
euler_circuit = generate_graph_with_euler_circuit(num_vertices)
print(list(euler_circuit))
