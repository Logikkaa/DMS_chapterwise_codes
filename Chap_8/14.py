from sage.graphs.graph_generators import graphs
from sage.graphs.graph_plot import crossing_number

# Generate K7,7 graph
G = graphs.CompleteBipartiteGraph(7, 7)

# Calculate the crossing number
crossings = crossing_number(G)
print("Crossing Number of K7,7:", crossings)
