with open('input.txt', 'r') as f:
    maxElf = 0
    currentElf = 0
    while True:
        currentCalorie = f.readline()
        print(currentCalorie)
        if not currentCalorie:
            break
        if currentCalorie == '\n' :
            if  currentElf > maxElf:
                maxElf = currentElf
            currentElf = 0
            continue
        currentElf = currentElf + int(currentCalorie)
    print(maxElf)