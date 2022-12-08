def deepSumSize(dict):
    suma = 0
    for key in dict:
        print(key)
        if key == 'size' :
            if  dict[key] < 100000:
                suma += int(dict[key])
        else:
            suma += deepSumSize(dict[key])
    return suma

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
                # print('--------')
                # print(a)
                
        elif line.startswith('$ cd'):
            directoryName = line.split(' ')[2][:-1]
            if directoryName not in currentDirectories[-1]:
                currentDirectories[-1][directoryName] = {'size' : 0}
            currentDirectories.append(currentDirectories[-1][directoryName])
    
        if line[0].isdigit():
            # print(line)
            # print(currentDirectories)
            memoryUsed = int(line.split(' ')[0])
            for directory in currentDirectories:
                # print(directory)
                directory['size'] = directory['size'] + memoryUsed
                
                
    

    # print directories to json
    points = deepSumSize(directories)
    
    print(points)