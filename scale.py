# returns the intervals in terms of half tones
def getIntervals(scaleName):
    if scaleName.lower() == "major":
        return [2, 2, 1, 2, 2, 2, 1]
    elif scaleName.lower() == "minor":
        return [2, 1, 2, 2, 1, 2, 2]
    elif scaleName.lower() == "harmonic minor":
        return [2, 1, 2, 2, 1, 3, 1]
    elif scaleName.lower() == "minor pentatonic":
        return [3, 2, 2, 3, 2]
    elif scaleName.lower() == "major pentatonic":
        return [2, 2, 3, 2, 3]
    elif scaleName.lower() == "blues scale":
        return [3, 2, 1, 1, 3, 2]
    elif scaleName.lower() == "ionian":
        return [2, 2, 1, 2, 2, 2, 1]
    elif scaleName.lower() == "dorian":
        return [2, 1, 2, 2, 2, 1, 2]
    elif scaleName.lower() == "phrygian":
        return [1, 2, 2, 2, 1, 2, 2]
    elif scaleName.lower() == "lydian":
        return [2, 2, 2, 1, 2, 2, 1]
    elif scaleName.lower() == "mixolydian":
        return [2, 2, 1, 2, 2, 1, 2]
    elif scaleName.lower() == "aeolian":
        return [2, 1, 2, 2, 1, 2, 2]
    elif scaleName.lower() == "locrian":
        return [1, 2, 2, 1, 2, 2, 2]

def getScale(tonic, intervals):
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    for i in range(0, int(len(notes)/2 - 1)):
        if notes[i].lower() == tonic.lower():
            rootIndex = i
            break
    scaleOutput = [notes[rootIndex]]

    for i in range(0, len(intervals)):
        rootIndex += intervals[i]
        scaleOutput.append(notes[rootIndex])
    return scaleOutput

if __name__ == "__main__":
    intervals = getIntervals("harmonic minor")
    print(intervals)
    print(getScale("A", intervals))
