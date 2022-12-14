file = open('input.txt')

grid = set()

maxY = -1

for line in file:
    points = line.strip().split("->")
    curr = [int(val) for val in points[0].split(",")]
    for i in range(1, len(points)):
        next = [int(val) for val in points[i].split(",")]
        if curr[0] == next[0]:
            for j in range(min(curr[1], next[1]), max(curr[1], next[1]) + 1):
                grid.add((curr[0], j))
            if max(curr[1], next[1]) > maxY:
                maxY = max(curr[1], next[1])
        else:
            if curr[1] > maxY:
                maxY = curr[1]
            for j in range(min(curr[0], next[0]), max(curr[0], next[0]) + 1):
                grid.add((j, curr[1]))
        curr = next

sandPile = set()
infinite = False
while not infinite:
    sandPos = (500, 0)
    moving = True
    while moving:
        checkPos = (sandPos[0], sandPos[1] + 1)
        checkLeft = (sandPos[0] - 1, sandPos[1] + 1)
        checkRight = (sandPos[0] + 1, sandPos[1] + 1)
        if checkPos[1] == maxY + 2:
            moving = False
        elif checkPos not in grid:
            sandPos = checkPos
        elif checkLeft not in grid:
            sandPos = checkLeft
        elif checkRight not in grid:
            sandPos = checkRight
        else:
            moving = False
    if sandPos == (500, 0):
        sandPile.add(sandPos)
        break
    if not infinite:
        sandPile.add(sandPos)
        grid.add(sandPos)
print(len(sandPile))