with open('input.txt', 'r') as f:
    points = 0
    moves = {
        "X" : 'LOSE',
        "A" : 'ROCK',
        "Y": 'DRAW',
        "B": 'PAPER',
        "Z": 'WIN',
        "C": 'SCISSORS'
    }
    movePoints = {
        "ROCK" : 1,
        "PAPER" : 2,
        "SCISSORS" : 3,
        "WIN": 6,
        "DRAW": 3,
        "LOSE": 0
    }
    currentElf = 0
    while True:
        currentmove = f.readline()
        if not currentmove:
            break
        enemyAttack = moves[currentmove[0]]
        shouldDo = moves[currentmove[2]]
        points = points + movePoints[shouldDo]
        if shouldDo == 'DRAW':
            points = points + movePoints[enemyAttack]
        elif shouldDo == 'WIN':
            points = points + ((movePoints[enemyAttack] + 1) % 3 or 3)
        elif shouldDo == 'LOSE':
            points = points + ((movePoints[enemyAttack] - 1) % 3 or 3)
    print(points)