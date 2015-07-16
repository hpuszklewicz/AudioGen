import random


def pmf(p, rand, prev = 0):
    firstProb = p[0][1]
    if firstProb >= (rand - prev):
        return p[0][0]
    else:
        return pmf(p[1:],
                   rand = rand - prev,
                   prev = firstProb)


class Vertex:
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


class Graph:
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
        self.probs = {}
        self.curr = None

    def addState(self, name):
        self.vertices[name] = Vertex(name)

    def connect(self, name1, name2, weight):
        if weight < 0 or weight > 1:
            raise ValueError("Weights in the chain must be between 0 and 1, inclusive")
        vertex1, vertex2 = self.vertices[name1], self.vertices[name2]
        vertex1.connectTo(vertex2, weight)
        if not self._checkNeighborhoodSums():
            raise ValueError("Sum of neighborhood edges must be between 0 and 1, inclusive")
                
    def _checkNeighborhoodSums(self, start = False):
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
        if not self._checkNeighborhoodSums(start = True):
            raise ValueError("The probability of a state switching must be 1")
        if startState is None:
            self.curr = random.choice(list(self.vertices.keys()))
        else:
            self.curr = startState
        
        def getProbDist(state):
            probDistribution = []
            neighbors = self.vertices[state].neighbors
            for neighbor in neighbors:
                probDistribution.append((neighbor.name, neighbors[neighbor]))
            return probDistribution

        for vertex in self.vertices:
            self.probs[vertex] = getProbDist(vertex)

    def nextState(self):
        probDistribution = self.probs[self.curr]
        nextState = pmf(probDistribution, random.random())
        self.curr = nextState
        return nextState

    def getStates(self, n, start = None):
        if start is None:
            self.start()
        else:
            self.start(start)
        states = []
        for x in range(n):
            states.append(self.nextState())
        return states

if __name__ == "__main__":
    
    g = Graph()
    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("C")
    g.connect("A", "B", 0.23)
    g.connect("A", "C", 0.3)
    g.connect("B", "C", 0.2)
    print("Undirected graph: ")
    print(g)

    dg = DirectedGraph()
    dg.addVertex("A")
    dg.addVertex("B")
    dg.addVertex("C")
    dg.connect("A", "B", 0.23)
    dg.connect("A", "C", 0.3)
    dg.connect("B", "C", 0.2)
    print("Directed graph: ")
    print(dg)

    mc = MarkovChain()
    mc.addState("A")
    mc.addState("B")
    mc.addState("C")
    mc.addState("D")
    mc.addState("E")
    mc.addState("F")

    mc.connect("A", "A", 0.1)
    mc.connect("A", "B", 0.15)
    mc.connect("A", "C", 0.2)
    mc.connect("A", "D", 0.05)
    mc.connect("A", "E", 0.25)
    mc.connect("A", "F", 0.25)

    mc.connect("B", "F", 0.025)
    mc.connect("B", "E", 0.025)
    mc.connect("B", "D", 0.05)
    mc.connect("B", "C", 0.1)
    mc.connect("B", "B", 0.1)
    mc.connect("B", "A", 0.7)

    mc.connect("C", "C", 0.3)
    mc.connect("C", "D", 0.4)
    mc.connect("C", "E", 0.3)

    mc.connect("D", "E", 0.35)
    mc.connect("D", "F", 0.15)
    mc.connect("D", "B", 0.5)

    mc.connect("E", "D", 0.2) 
    mc.connect("E", "F", 0.2)
    mc.connect("E", "A", 0.6) 

    mc.connect("F", "B", 0.75)
    mc.connect("F", "C", 0.25)

    print("Markov Chain: ")
    print(mc)

    print("Generating 1000 states from chain: ")
    states = mc.getStates(1000)
    print(states)
    
    
