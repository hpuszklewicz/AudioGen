# equally spaces the amount of desired pulses(or hits)
# into the amount of desired steps(or beats)
def bjorklund(steps, pulses):
    if pulses > steps:
        raise ValueError("Pulses cannot be greater than steps")
    divisor = steps - pulses
    remainder = [pulses]
    level = 0
    count = []

    while True:
        count.append(divisor/remainder[level])
        remainder.append(divisor % remainder[level])
        divisor = remainder[level]
        level += 1
        if remainder[level] <= 1:
            break
    count.append(divisor)

    rhythm = []
    def build(level):
        if level == -1:
            rhythm.append("0")
        elif level == -2:
            rhythm.append("1")
        else:
            for i in range(0, int(count[level])):
                build(level - 1)
            if remainder[level] != 0:
                build(level - 2)
    build(level)
    i = rhythm.index("1")
    rhythm = rhythm[i:] + rhythm[0:i]
    return rhythm

def toString(list):
    rhythmString = ""
    for i in range(0, len(list)):
        rhythmString += list[i]
    return rhythmString



if __name__ == '__main__':
    print(bjorklund(16, 7))
    print(toString(bjorklund(16, 7)))

