import networkx as nx
from itertools import combinations

def generate_all_simple_graphs(n):
    graphs = []
    for edges in combinations(range(n), 2):
        G = nx.Graph()
        G.add_edges_from([edges])
        graphs.append(G)
    return graphs

n = 4
graphs = generate_all_simple_graphs(n)
for G in graphs:
    print(G.edges())
