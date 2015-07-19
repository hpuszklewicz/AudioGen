import scale, music21 as m21
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
        while sum(currTime)/4 < ((self.tempo)/60.0)*self.length:
            pickedNote = random.choice(self.scale)
            pickedTime = random.choice([2, 1, .5, .25])
            currTime.append(pickedTime)
            result.append((pickedNote, pickedTime))
        print(sum(currTime))
        return result

    def generateSound(self):
        pass

    def playBack(self):
        playBackStream = m21.stream.Stream()
        noteStream = self.noteStream
        for i in range(len(noteStream)):
            newNote = m21.note.Note(noteStream[i][0]+ "4")
            newNote.duration.type = m21.duration.convertQuarterLengthToType(noteStream[i][1])
            playBackStream.append(newNote)
        return playBackStream
    
if __name__=='__main__':
    scale = scale.getScale("A", "harmonic minor") 
    test1 = ProcGen(30, scale, 40, "N/A", "N/A")
    print(test1.noteStream)
    print(test1.noteStream[1][0])
    newStream = test1.playBack()
    newStream.show()
    
