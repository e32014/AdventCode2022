file = open('input.txt')
rounds = 0
elves = set()
considerOrder = ['N', 'S', 'W', 'E']
y = 0
for line in file:
    x = 0
    for char in line.strip():
        if char == '#':
            elves.add((x, y))
        x += 1
    y += 1
print(elves)

while True:
    proposals = dict()
    dupe_check = dict()
    for elf_x, elf_y in elves:
        countNearby = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x, y) == (0, 0):
                    continue
                elif (elf_x + x, elf_y + y) in elves:
                    countNearby += 1
        if countNearby == 0:
            proposals[(elf_x, elf_y)] = (elf_x, elf_y)
            dupe_check[(elf_x, elf_y)] = dupe_check.get((elf_x, elf_y), 0) + 1
        else:
            for dir in considerOrder:
                if dir == 'N' and (elf_x - 1, elf_y - 1) not in elves and (elf_x, elf_y - 1) not in elves and (elf_x + 1, elf_y - 1) not in elves:
                    proposals[(elf_x, elf_y)] = (elf_x, elf_y - 1)
                    dupe_check[(elf_x, elf_y - 1)] = dupe_check.get((elf_x, elf_y - 1), 0) + 1
                    break
                elif dir == 'S' and (elf_x - 1, elf_y + 1) not in elves and (elf_x, elf_y + 1) not in elves and (elf_x + 1, elf_y + 1) not in elves:
                    proposals[(elf_x, elf_y)] = (elf_x, elf_y + 1)
                    dupe_check[(elf_x, elf_y + 1)] = dupe_check.get((elf_x, elf_y + 1), 0) + 1
                    break
                elif dir == 'W' and (elf_x - 1, elf_y - 1) not in elves and (elf_x - 1, elf_y) not in elves and (elf_x - 1, elf_y + 1) not in elves:
                    proposals[(elf_x, elf_y)] = (elf_x - 1, elf_y)
                    dupe_check[(elf_x - 1, elf_y)] = dupe_check.get((elf_x - 1, elf_y), 0) + 1
                    break
                elif dir == 'E' and (elf_x + 1, elf_y - 1) not in elves and (elf_x + 1, elf_y) not in elves and (elf_x + 1, elf_y + 1) not in elves:
                    proposals[(elf_x, elf_y)] = (elf_x + 1, elf_y)
                    dupe_check[(elf_x + 1, elf_y)] = dupe_check.get((elf_x + 1, elf_y), 0) + 1
                    break
        if (elf_x, elf_y) not in proposals:
            proposals[(elf_x, elf_y)] = (elf_x, elf_y)
            dupe_check[(elf_x, elf_y)] = dupe_check.get((elf_x, elf_y), 0) + 1

    new_poses = set()
    for elf, proposal in proposals.items():
        if dupe_check[proposal] > 1:
            new_poses.add(elf)
        else:
            new_poses.add(proposal)
    if len(elves.intersection(new_poses)) == len(elves):
        print(rounds + 1)
        break
    elves = new_poses
    considerOrder = considerOrder[1:] + list(considerOrder[0])

    if rounds == 9:
        maxX = -1000000000000
        minX = 1000000000000
        maxY = maxX
        minY = minX
        for elf_x, elf_y in elves:
            if elf_x > maxX:
                maxX = elf_x
            if elf_x < minX:
                minX = elf_x
            if elf_y > maxY:
                maxY = elf_y
            if elf_y < minY:
                minY = elf_y
        print((maxX - minX + 1) * (maxY - minY + 1) - len(elves))

    rounds += 1