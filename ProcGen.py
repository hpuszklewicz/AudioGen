class ProcGen():
    def __init__(self, length, scale, tempo, chordprog, voices):
        self.length = length
        self.scale = scale
        self.tempo = tempo
        self.chordprog = chordprog
        self.voices = voices
        self.noteStream = self.generateNotes()
        
    def generateNotes(self):
        import random
        currTime = []
        result = []
        while sum(currTime) < ((self.tempo)/60.0)*self.length:
            pickedNote = random.choice(self.scale)
            pickedTime = random.choice([0.5, 0.25, 0.125, 0.0625])
            currTime.append(pickedTime)
            result.append((pickedNote, pickedTime))
        print sum(currTime)
        return result

    def generateSound(self):
        pass
        

if __name__=='__main__':
    test1 = ProcGen(30, ["A", "B", "C", "D", "E", "F", "G"], 40, "N/A", "N/A")
    print test1.noteStream

    
