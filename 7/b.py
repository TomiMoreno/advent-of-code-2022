neededSpace = 30000000
TOTAL_SPACE = 70000000
def deepSumSize(t, ocupiedSpace = 0, smallest = 1000000000000000):
    for key in t:
        current = t[key]
        if key == 'size':
            freeSpace =  TOTAL_SPACE - (ocupiedSpace - current)

            if  freeSpace > neededSpace and current < smallest:
                print(freeSpace)
                print(current)
                print('-----------------')
                smallest = current
        elif type(current) == dict:
            nsmallest = deepSumSize(current, ocupiedSpace=ocupiedSpace, smallest=smallest)
            if nsmallest < smallest:
                smallest = nsmallest
    return smallest

with open('input.txt', 'r') as f:
    memory = 0
    letters = []
    directories = { '/': {'size': 0}}
    currentDirectories = [directories['/']]
    lessThan10000 = []
    while True: 
        line = f.readline()
        if not line:
            break
        if line.startswith('$ cd ..'):
            if len(currentDirectories) > 0:
                a = currentDirectories.pop()
                
        elif line.startswith('$ cd'):
            directoryName = line.split(' ')[2][:-1]
            if directoryName not in currentDirectories[-1]:
                currentDirectories[-1][directoryName] = {'size' : 0}
            currentDirectories.append(currentDirectories[-1][directoryName])
    
        if line[0].isdigit():
            memoryUsed = int(line.split(' ')[0])
            for directory in currentDirectories:
                # print(directory)
                directory['size'] = directory['size'] + memoryUsed
                
                
    

    # print directories to json
    points = deepSumSize(directories, ocupiedSpace=directories['/']['size'])
    
    print(points)