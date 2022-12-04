with open('input.txt', 'r') as f:
    points = 0
    moves = {
        "X" : 'ROCK',
        "A" : 'ROCK',
        "Y": 'PAPER',
        "B": 'PAPER',
        "Z": 'SCISSORS',
        "C": 'SCISSORS'
    }
    currentElf = 0
    while True:
        currentmove = f.readline()
        if not currentmove:
            break
        print(currentmove)
        enemyAttack = moves[currentmove[0]]
        myAttack = moves[currentmove[2]]
        if enemyAttack == myAttack:
            points = points + 3
        elif enemyAttack == 'ROCK' and myAttack == 'PAPER':
            points = points + 6
        elif enemyAttack == 'PAPER' and myAttack == 'SCISSORS':
            points = points + 6
        elif enemyAttack == 'SCISSORS' and myAttack == 'ROCK':
            points = points + 6
        if myAttack == 'ROCK':
            points = points + 1
        elif myAttack == 'PAPER':
            points = points + 2
        elif myAttack == 'SCISSORS':
            points = points + 3
    print(points)