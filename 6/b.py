
def hasRepeatedElements(arr):
    elements = set()
    for i in arr:
        if i in elements:
            return True
        elements.add(i)
        
    return False

with open('input.txt', 'r') as f:
    position = 1
    line = f.readline()
    letters = []
    for l in line:
        if len(letters) > 13:
            letters.pop(0)
        letters.append(l)
        if not hasRepeatedElements(letters) and len(letters) == 14:
           print(position) 
        position += 1
    
    print(position)
