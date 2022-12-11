with open('input.txt', 'r') as f:
  matrix = []
  max = 0

  def checkPos(i, j):
    width = len(matrix)
    row = matrix[i]
    v = row[j]
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    for t in reversed(range(i)):
      pos = matrix[t][j]
      y1 += 1
      if pos >= v:
        break
    for t in range(i+1, width):
      pos = matrix[t][j]
      y2 += 1
      if pos >= v:
        break
    for t in reversed(range(j)):
      pos = row[t]
      x1 += 1
      if pos >= v:
        break
    for t in range(j+1, len(row)):
      pos = row[t]
      x2 += 1
      if pos >= v:
        break
    return x1 * x2 * y1 * y2

  while True:
    line = f.readline()
    if not line:
      break
    treeHeights = []
    for n in [*line]:
      if n != '\n':
        treeHeights.append(int(n))
    matrix.append(treeHeights)

  for i in range(len(matrix)):
    row = matrix[i]
    for j in range(len(row)):
      p = checkPos(j, i)
      if p > max:
        max = p

  print(max)
