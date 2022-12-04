def letterPoints(l):
    charcode = ord(l)
    isUpper = charcode >= 65 and charcode <= 90
    return charcode - 38 if isUpper else charcode - 96

with open('input.txt', 'r') as f:
    points = 0
    while True:
        currentRucksack = f.readline()
        if not currentRucksack:
            break
        half = int(len(currentRucksack) / 2)
        firstHalf = currentRucksack[:half]
        secondHalf = currentRucksack[half:]
        for i in firstHalf:
            if i in secondHalf:
                points = points + letterPoints(i)
                break
    print(points)