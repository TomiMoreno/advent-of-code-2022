with open('input.txt', 'r') as f:
  matrix = []
  visibleTrees = 0
  while True:
    line = f.readline()
    if not line:
      break
    treeHeights = []
    for n in [*line]:
      if n != '\n':
        treeHeights.append({'h': int(n), 'v': False})
    matrix.append(treeHeights)

  for row in matrix:
    print(row)
    max = -1
    for tree in row:
      if tree['h'] > max:
        max = tree['h']
        tree['v'] = True
    max = -1
    for tree in row[::-1]:
      if tree['h'] > max:
        max = tree['h']
        tree['v'] = True

    for i in range(len(matrix)):
      max = -1
      for j in range(len(matrix[0])):
        tree = matrix[j][i]
        if tree['h'] > max:
          max = tree['h']
          tree['v'] = True
      max = -1
      for j in range(len(matrix[0]))[::-1]:
        tree = matrix[j][i]
        if tree['h'] > max:
          max = tree['h']
          tree['v'] = True

  for row in matrix:
    for tree in row:
      if tree['v']:
        visibleTrees += 1

  print(visibleTrees)
