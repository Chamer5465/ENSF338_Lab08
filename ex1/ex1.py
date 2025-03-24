class GraphNode:
    def __init__(self, data, index):
        self.data = data
        self.index = index

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = 0
        self.adjList = [[] for x in range(num_vertices)]

    def addEdge(self, n1, n2, weight):
        self.adjList[n1.index].append((n2, weight))
        self.adjList[n2.index].append((n1, weight))

    def removeEdge(self, n1, n2):
        for i in self.adjList[n1.index]:
            if i[0] == n2:
                self.adjList[n1.index].remove(i)
        for i in self.adjList[n2.index]:
            if i[0] == n1:
                self.adjList[n2.index].remove(i)
        
    def addNode(self, data):
        self.num_vertices += 1
        new_node = GraphNode(data, self.num_vertices)
        return new_node

    def removeNode(self, node):
        for i in node.adjList:
            self.removeEdge(node, i[0])
        self.num_vertices -= 1

    