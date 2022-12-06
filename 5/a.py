with open('input.txt', 'r') as f:
    result = ''
    cranes = []
    mode = 'craneCreating'
    
    
    while True:
        line = f.readline()
        if not line:
            break
        if mode == 'craneCreating':
            if line == '\n':
                mode = 'craneMoving'
                for crane in cranes:
                    crane.reverse()
                continue
            if len(cranes) == 0:
                cranes = ([[] for i in range(int(len(line) / 4))])
            for i in range(len(line)):
                if line[i].isupper() :
                    cranes[int(i / 4)].append(line[i])
        elif mode == 'craneMoving':
            print(cranes)
            if line == '\n':
                mode = 'cranePopping'
                continue
            move = int(line.split(' ')[1])
            fromCrane = int(line.split(' ')[3])
            toCrane = int(line.split(' ')[5])
            while move > 0 and len(cranes[fromCrane-1]) > 0:
                cranes[toCrane -1].append(cranes[fromCrane-1].pop())
                move = move - 1
    for crane in cranes:
        result += crane.pop()
    print(result)