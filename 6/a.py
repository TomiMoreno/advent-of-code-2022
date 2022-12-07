
def hasRepeatedElements(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

with open('input.txt', 'r') as f:
    position = 0
    line = f.readline()
    letters = []
    for l in line:
        if l in letters or len(letters) < 4 or hasRepeatedElements(letters):
            if len(letters) == 4:
                letters.pop(0)
            letters.append(l)
        else:
            print(''.join(letters))
            break
        position += 1
    
    print(position)
