import networkx as nx
import random

def generate_graph_with_hamilton_circuit(num_vertices):
    while True:
        G = nx.hamiltonian_cycle(nx.complete_graph(num_vertices))
        if G is not None:
            return G

num_vertices = 10
hamilton_circuit = generate_graph_with_hamilton_circuit(num_vertices)
print(list(hamilton_circuit))
