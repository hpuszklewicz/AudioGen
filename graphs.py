import random

def pmf(p, rand = None, sortedp = None, prev = 0):
    if rand is None:
        rand = random.random()
    sortedp = sorted(p, key = lambda x: x[1], reverse = True)
    if sortedp[0][1] >= (rand - prev): 
        return sortedp[0][0]
    else:
        return pmf(sortedp[1:],
                             rand = rand - prev,
                             sortedp = sortedp,
                             prev = sortedp[0][1])
    
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

    def start(self, startState = None):
        if startState is None:
            self.curr = random.choice(list(self.vertices.keys()))
        else:
            self.curr = startState

    def nextState(self):
        print self.curr
        neighbors = self.vertices[self.curr].neighbors
        for neighbor in neighbors:
            print neighbors[neighbor]

if __name__ == "__main__":
    
    g = Graph()
    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("C")
    g.connect("A", "B", 0.23)
    g.connect("A", "C", 0.3)
    g.connect("B", "C", 0.2)
    print g

    dg = DirectedGraph()
    dg.addVertex("A")
    dg.addVertex("B")
    dg.addVertex("C")
    dg.connect("A", "B", 0.23)
    dg.connect("A", "C", 0.3)
    dg.connect("B", "C", 0.2)
    print dg

    mc = MarkovChain()
    mc.addState("A")
    mc.addState("B")
    mc.addState("C")
    mc.connect("A", "B", 0.23)
    mc.connect("A", "C", 0.3)
    mc.connect("B", "C", 0.2)
    print mc

    mc.start()
    mc.nextState()

    print "\n\nPDF testing"
    
    from collections import Counter
    p = [("A", 0.25), ("B", 0.70), ("C", 0.05)]

    results = []
    for x in xrange(1000):
        results.append(pmf(p))

    print Counter(results)
