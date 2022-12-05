with open('input.txt', 'r') as f:
    points = 0
    while True:
        elvePair = f.readline()
        if not elvePair:
            break
        firstRange = [int(x) for x in  elvePair.split(',')[0].split('-')] 
        secondRange = [int(x) for x in  elvePair.split(',')[1].split('-')] 
        hasOverlap = False
        if firstRange[0] <= secondRange[0] <= firstRange[1]:
            hasOverlap = True
        elif secondRange[0] <= firstRange[0] <= secondRange[1]:
            hasOverlap = True
        if hasOverlap:
            points = points + 1

    print(points)