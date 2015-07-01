class MarkovChain():
    def __init__(self):
        self.graph = Graph()

    def addState(self, state):
        self.graph.addVertex(Vertex(state))
    
    def connect(self, state1, state2, weight):
        if weight < 0 or weight > 1:
            raise ValueError("Weights in a markov chain must be between 0 and 1.")
        vertex1 = self.graph.vertices[state1]
        vertex2 = self.graph.vertices[state2]
        vertex1.connectTo(vertex2, weight)
        if not self.checkNeighborhoodSum():
            pass
        

    def checkNeighborhoodSum(self):
        graph = self.graph.vertices
        for vertex in graph:
            total = 0
            neighbors = graph[vertex].neighbors
            for neighbor in neighbors:
                total += neighbors[neighbor]
            if total > 1:
                return False
        return True
            
    def __str__(self):
        return self.graph.__str__()
        

class Vertex():
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def connectTo(self, vertex, weight):
        self.neighbors[vertex] = weight
        vertex.neighbors[self] = weight

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
    mc = MarkovChain()
    mc.addState("A")
    mc.addState("B")
    mc.addState("C")
    mc.addState("D")
    mc.connect("A", "B", 0.7)
    mc.connect("A", "C", 0.34)
    mc.connect("C", "D", 0.289)
    mc.connect("A", "A", 0.3)
    print mc
    mc.checkNeighborhoodSum()
