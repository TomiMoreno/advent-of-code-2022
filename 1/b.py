with open('input.txt', 'r') as f:
    top3Elfs = [0, 0, 0]
    currentElf = 0
    while True:
        currentCalorie = f.readline()
        if not currentCalorie:
            break
        if currentCalorie == '\n' :
            if  currentElf > top3Elfs[2]:
                top3Elfs[2] = currentElf
                top3Elfs.sort(reverse=True)
            currentElf = 0
            continue
        currentElf = currentElf + int(currentCalorie)
    print(sum(top3Elfs))