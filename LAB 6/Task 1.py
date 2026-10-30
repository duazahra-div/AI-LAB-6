class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.adj[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * self.V
        self.DFSUtil(v, visited)


g = Graph(13)

g.addEdge(1, 2)
g.addEdge(1, 7)
g.addEdge(1, 8)

g.addEdge(2, 3)
g.addEdge(2, 6)

g.addEdge(3, 4)
g.addEdge(3, 5)

g.addEdge(8, 9)
g.addEdge(8, 12)

g.addEdge(9, 10)
g.addEdge(9, 11)

print("Following is Depth First Traversal:")
g.DFS(1)