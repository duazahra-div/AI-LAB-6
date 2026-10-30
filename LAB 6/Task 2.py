class Graph:
    def __init__(self):
        self.adj = {}

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []

        if w not in self.adj:
            self.adj[w] = []

        self.adj[v].append(w)

    def DFS(self, start, goal):
        stack = [start]
        visited = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.append(node)
                print(node, end=" ")

                if node == goal:
                    print("\nGoal found:", goal)
                    return

                for child in reversed(self.adj[node]):
                    if child not in visited:
                        stack.append(child)

        print("\nGoal not found")


g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

g.addEdge('B', 'K')
g.addEdge('B', 'J')

g.addEdge('K', 'N')
g.addEdge('K', 'M')

g.addEdge('D', 'G')

g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')

g.addEdge('I', 'L')

print("DFS Traversal:")
g.DFS('A', 'Z')