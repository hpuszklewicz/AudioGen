class MarkovChain():
    import random
    def __init__(self, chain, curr = None):
        self.chain = chain
        self.currState = random.choice(chain) if curr is not None else curr

    def nextState(given = None):
        if given == None:
            currIndex = self.chain.index(self.currState)
            return self.chain[currIndex + 1]
        
