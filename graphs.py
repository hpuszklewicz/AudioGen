import random

class Vertex():
    def __init__(self, name, directed = False):
        self.name = name
        self.neighbors = {}
        self.directed = directed

    def connectTo(self, vertex, weight):
        self.neighbors[vertex] = weight

    def disconnectFrom(self, vertex):
        self.neighbors.pop(vertex, None)

    def __str__(self):
        info = ""
        if len(self.neighbors) == 0:
            return self.name + " is isolated."
            info += self.name + " is connected to: "
            for neighbor in self.neighbors:
                info += "(" + neighbor.name + ", " 
                info += str(self.neighbors[neighbor]) + ") "
                return info

class Graph():
    def __init__(self):
        self.vertices = {}
        self.directed = False
        
    def addVertex(self, name):
        self.vertices[name] = Vertex(name)

    def connect(self, name1, name2, weight):
        vertex1, vertex2 = self.vertices[name1], self.vertices[name2]
        vertex1.connectTo(vertex2, weight)
        vertex2.connectTo(vertex1, weight)

    def disconnect(self, name1, name2):
        vertex1, vertex2 = self.vertices[name1], self.vertices[name2]
        vertex1.disconnectFrom(vertex2)
        vertex2.disconnectFrom(vertex1)

    def __str__(self):
        info = ""
        for vertex in self.vertices:
            info += vertex + ": "
            neighbors = self.vertices[vertex].neighbors
            for neighbor in neighbors:
                info += "(" + neighbor.name + ", " 
                info += str(neighbors[neighbor]) + ") "
                info += "\n"
                return info

class DirectedGraph(Graph):
    def __init__(self):
        Graph.__init__(self)

    def connect(self, name1, name2, weight):
        vertex1, vertex2 = self.vertices[name1], self.vertices[name2]
        vertex1.connectTo(vertex2, weight)

    def disconnect(self, name1, name2):
        vertex1, vertex2 = self.vertices[name1], self.vertices[name2]
        vertex1.disconnectFrom(vertex2)

class MarkovChain(DirectedGraph):
    def __init__(self):
        DirectedGraph.__init__(self)

    def addState(self, name):
        self.vertices[name] = Vertex(name)

    def connect(self, name1, name2, weight):
        if weight < 0 or weight > 1:
            raise ValueError("Weights in the chain must be between 0 and 1, inclusive")
            vertex1, vertex2 = self.vertices[name1], self.vertices[name2]
            vertex1.connectTo(vertex2, weight)
            if not self.checkNeighborhoodSums():
                raise ValueError("Sum of neighborhood edges must be between 0 and 1, inclusive")
                
    def checkNeighborhoodSums(self):
        for vertex in self.vertices:
            total = 0
            neighbors = self.vertices[vertex].neighbors
            for neighbor in neighbors:
                total += neighbors[neighbor]
                if total > 1:
                    return False
                    return True
                    

if __name__ == "__main__":
    
    mc = MarkovChain()
    mc.addState("A")
    print mc
    mc.addState("B")
    mc.addState("C")
    mc.connect("A", "B", 0.2)
    mc.connect("B", "A", 0.1)
    mc.connect("A", "C", 0.78)
    print mc
