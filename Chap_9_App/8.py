from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def strongly_connected_components(self):
        visited = [False] * self.V
        stack = []
        scc = []

        def dfs(u):
            visited[u] = True
            stack.append(u)

            for v in self.graph[u]:
                if not visited[v]:
                    dfs(v)
            
            return
        
        for i in range(self.V):
            if not visited[i]:
                dfs(i)

        transposed_graph = self.transpose()

        visited = [False] * self.V

        while stack:
            u = stack.pop()
            if not visited[u]:
                scc_group = []
                transposed_graph.dfs(u, visited, scc_group)
                scc.append(scc_group)
        
        return scc

    def dfs(self, u, visited, scc_group):
        visited[u] = True
        scc_group.append(u)

        for v in self.graph[u]:
            if not visited[v]:
                self.dfs(v, visited, scc_group)
        
        return
    
    def transpose(self):
        transposed = Graph(self.V)

        for u in self.graph:
            for v in self.graph[u]:
                transposed.add_edge(v, u)

        return transposed

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:", g.strongly_connected_components())
