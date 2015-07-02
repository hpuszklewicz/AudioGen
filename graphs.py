import random

class MarkovChain():
    def __init__(self):
        self.graph = Graph()
        self.curr = None

    def addState(self, state):
        self.graph.addVertex(Vertex(state))
    
    def connect(self, state1, state2, weight):
        if weight < 0 or weight > 1:
            raise ValueError("Weights in a markov chain must be between 0 and 1.")
        vertex1 = self.graph.vertices[state1]
        vertex2 = self.graph.vertices[state2]
        vertex1.connectTo(vertex2, weight)
        if not self.checkNeighborhoodSums():
            vertex1.disconnectFrom(vertex2)
            raise ValueError("Sum of neighborhood edges must be between 0 and 1.")

    def getNeighborhoodSum(self, vertex):
        total = 0
        graph = self.graph.vertices
        neighbors = graph[vertex].neighbors
        for neighbor in neighbors:
            total += neighbors[neighbor]
        return total

    def checkNeighborhoodSums(self):
        graph = self.graph.vertices
        for vertex in graph:
            total = 0
            neighbors = graph[vertex].neighbors
            for neighbor in neighbors:
                total += neighbors[neighbor]
            if total > 1:
                return False
        return True

    def start(self, start = None):
        choices = self.graph.vertices
        if start is None:
            self.curr = random.choice(list(choices.keys()))
        else:
            self.curr = start
        print "Starting at: " + self.curr

    def getNextState(self):
        choices = self.graph.vertices
        nextChoices = choices[self.curr]
        for choice in nextChoices.neighbors:
            print self.getNeighborhoodSum(choice.name)
            
    def __str__(self):
        return self.graph.__str__()
        

class Vertex():
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def connectTo(self, vertex, weight):
        self.neighbors[vertex] = weight
        vertex.neighbors[self] = weight

    def disconnectFrom(self, vertex):
        self.neighbors.pop(vertex, None)

    def __str__(self):
        info = ""
        info += self.name + " is connected to: "
        for neighbor in self.neighbors:
            info += "(" + neighbor.name + ", " 
            info += str(self.neighbors[neighbor]) + ") "
        return info

class Graph():
    def __init__(self):
        self.vertices = {}
    
    def addVertex(self, vertex):
        self.vertices[vertex.name] = vertex

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

if __name__=='__main__':
    g = Graph()
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v4 = Vertex("D")
    v1.connectTo(v2, 3)
    print v1
    v1.disconnectFrom(v2)
    print v1

    mc = MarkovChain()
    mc.addState("A")
    mc.addState("B")
    mc.addState("C")
    mc.addState("D")
    mc.connect("A", "B", 0.34)
    print mc
    mc.connect("A", "C", 0.65)
    print mc
    mc.connect("B", "D", 0.22394)
    print mc
    try:
        mc.connect("A", "D", 0.04)
    except ValueError:
        print "Perfect"
    print mc

    mc.start()
    mc.getNextState()
