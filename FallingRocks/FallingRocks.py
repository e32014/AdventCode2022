file = open('input.txt')

# Rocks are recorded from the bottom left corner of the rock
rocks = [((0, 0), (1, 0), (2, 0), (3, 0)),
         ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
         ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
         ((0, 0), (0, 1), (0, 2), (0, 3)),
         ((0, 0), (1, 0), (0, 1), (1, 1))]
rockPos = 0

jetpattern = file.readline().strip()
jetPos = 0

chamber = set()
currMax = -1

currPos = (2, 3)
reps = 1_000_000_000_000
size = 7
y_ups = dict()
y_down = dict()
dropped = 0
additional = 0
seen = dict()
while dropped < reps:
    while True:
        rock = rocks[rockPos]
        posPos = currPos
        if jetpattern[jetPos] == '<':
            posPos = (posPos[0] - 1, posPos[1])
        elif jetpattern[jetPos] == '>':
            posPos = (posPos[0] + 1, posPos[1])
        jetPos = (jetPos + 1) % len(jetpattern)
        if any([coord_x + posPos[0] < 0 or coord_x + posPos[0] >= size or (coord_x + posPos[0], coord_y + posPos[1]) in chamber for coord_x, coord_y in rock]):
            posPos = currPos
        posPos = (posPos[0], posPos[1] - 1)
        if posPos[1] < 0 or any([(coord_x + posPos[0], coord_y + posPos[1]) in chamber for coord_x, coord_y in rock]):
            dropped += 1
            for coord_x, coord_y in rock:
                chamber.add((coord_x + posPos[0], coord_y + posPos[1] + 1))
                if coord_y + posPos[1] + 1 > currMax:
                    currMax = coord_y + posPos[1] + 1
                if y_down.get(coord_x + posPos[0], -1) < coord_y + posPos[1] + 1:
                    y_down[coord_x + posPos[0]] = coord_y + posPos[1] + 1
            tops = tuple([y_down.get(i, -1) - currMax for i in range(7)])
            rockPos = (rockPos + 1) % len(rocks)
            currPos = (2, currMax + 4)
            if (tops, jetPos, rockPos) in seen:
                oldrocks, oldmax = seen[(tops, jetPos, rockPos)]
                repeat = (reps - dropped) // (dropped - oldrocks)
                dropped += repeat * (dropped - oldrocks)
                additional += repeat * (currMax - oldmax)
                seen = dict()
            seen[(tops, jetPos, rockPos)] = (dropped, currMax)
            break
        else:
            currPos = posPos
print(currMax + 1 + additional)