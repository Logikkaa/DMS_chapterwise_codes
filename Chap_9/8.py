import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to represent the game tree
# For a complete example, you need to add nodes and edges based on the rules of checkers

# Visualize the graph
pos = nx.spring_layout(G, seed=42)  # Adjust layout algorithm as needed
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
plt.show()
