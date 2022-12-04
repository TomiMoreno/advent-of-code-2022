def letterPoints(l):
    charcode = ord(l)
    isUpper = charcode >= 65 and charcode <= 90
    return charcode - 38 if isUpper else charcode - 96

with open('input.txt', 'r') as f:
    points = 0
    elfGroup = []
    while True:
        currentRucksack = f.readline()
        if not currentRucksack:
            break
        if(len(elfGroup) < 2):
            elfGroup.append(currentRucksack)
            continue
        elfGroup.append(currentRucksack)
        for i in elfGroup[0]:
            if i in elfGroup[1] and i in elfGroup[2]:
                points = points + letterPoints(i)
                break
        elfGroup = []
    print(points)