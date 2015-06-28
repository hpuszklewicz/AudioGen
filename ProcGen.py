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
        while sum(currTime) < self.length:
            pickedNote = random.choice(self.scale)
            pickedTime = random.choice([1/16, 1/8, 1/4, 1/2])
            currTime.append(pickedTime)
            result.append((pickedNote, pickedTime))
        return result

    def generateSound(self):
        pass
        

if __name__=='__main__':
    import music21
    test1 = ProcGen(20, ["A", "B", "C", "D", "E", "F", "G"], 110, "N/A", "N/A")
    print(music21.note)
    
