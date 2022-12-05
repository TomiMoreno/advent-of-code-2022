with open('input.txt', 'r') as f:
    points = 0
    while True:
        elvePair = f.readline()
        if not elvePair:
            break
        firstRange = [int(x) for x in  elvePair.split(',')[0].split('-')] 
        secondRange = [int(x) for x in  elvePair.split(',')[1].split('-')] 
        if (firstRange[0] <= secondRange[0] and firstRange[1] >= secondRange[1]):
            points = points + 1
        elif (secondRange[0] <= firstRange[0] and secondRange[1] >= firstRange[1]):
            points = points + 1

    print(points)