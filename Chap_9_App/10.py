class Hypercube:
    def __init__(self, dimension):
        self.dimension = dimension
        self.nodes = 2 ** dimension
        self.edges = self.generate_edges()

    def generate_edges(self):
        edges = []
        for i in range(self.nodes):
            for j in range(i + 1, self.nodes):
                diff = i ^ j
                if bin(diff).count('1') == 1:
                    edges.append((i, j))
        return edges

# Example usage
dimension = 3
hypercube = Hypercube(dimension)
print("Nodes:", hypercube.nodes)
print("Edges:", hypercube.edges)
