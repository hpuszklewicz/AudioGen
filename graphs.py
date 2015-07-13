import random
import string
import time
from collections import Counter
from collections import defaultdict

def pmf(p, rand, prev = 0):
    firstProb = p[0][1]
    if firstProb >= (rand - prev): 
        return p[0][0]
    else:
        return pmf(p[1:],
                   rand = rand - prev,
                   prev = firstProb)
    
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
                
    def checkNeighborhoodSums(self, start = False):
        for vertex in self.vertices:
            total = 0
            neighbors = self.vertices[vertex].neighbors
            for neighbor in neighbors:
                total += neighbors[neighbor]
            if start:
                if total != 1:
                    return False
            if total > 1:
                return False
        return True

    def start(self, startState = None):
        if not self.checkNeighborhoodSums(start = True):
            raise ValueError("Neighborhoods must have a sum of 1 before starting.")
        if startState is None:
            self.curr = random.choice(list(self.vertices.keys()))
        else:
            self.curr = startState

    def nextState(self):
        probDistribution = []
        neighbors = self.vertices[self.curr].neighbors
        for neighbor in neighbors:
            probDistribution.append((neighbor.name, neighbors[neighbor]))
        nextState = pmf(probDistribution, random.random())
        self.curr = nextState
        return nextState

if __name__ == "__main__":
    
    g = Graph()
    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("C")
    g.connect("A", "B", 0.23)
    g.connect("A", "C", 0.3)
    g.connect("B", "C", 0.2)
    print(g)

    dg = DirectedGraph()
    dg.addVertex("A")
    dg.addVertex("B")
    dg.addVertex("C")
    dg.connect("A", "B", 0.23)
    dg.connect("A", "C", 0.3)
    dg.connect("B", "C", 0.2)
    print(dg)

    mc = MarkovChain()
    mc.addState("A")
    mc.addState("B")
    mc.addState("C")
    mc.connect("A", "B", 0.5)
    mc.connect("A", "A", 0.2)
    mc.connect("A", "C", 0.3)
    mc.connect("B", "C", 0.2)
    mc.connect("B", "A", 0.1)
    mc.connect("B", "B", 0.7)
    mc.connect("C", "A", 0.35)
    mc.connect("C", "B", 0.15)
    mc.connect("C", "C", 0.5)
    print(mc)

    mc.start("A")
    results = []
    
    s = time.time()
    for x in range(1000000):
        results.append(mc.nextState())
    e = time.time()
    print(e-s)
    
    print Counter(results)
