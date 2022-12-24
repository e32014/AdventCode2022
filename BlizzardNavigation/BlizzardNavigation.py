file = open('input.txt')

blizzards = set()
walls = set()
start = ()
end = ()
i = 0
farSide_x = 0
for line in file:
    j = 0
    farSide_x = len(line.strip())
    for char in line.strip():
        if i == 0 and char == '.':
            start = (j, i)
            walls.add((j, i-1))
        elif char == '.':
            end = (j, i)
        elif char == '#':
            walls.add((j, i))
        elif char == '<' or char == '>' or char == 'v' or char == '^':
            blizzards.add((j, i, char))
        j += 1
    i += 1
farSide_y = i
walls.add((end[0], end[1] + 1))
queue = [(start, frozenset(blizzards), 0, 0)]
stormAtTime = {0: blizzards}
seen = set()
currIncr = 0
for end in [end, start, end]:
    while len(queue) != 0:
        (curr_x, curr_y), curr_storm, time, ends = queue.pop(0)
        if ((curr_x, curr_y), curr_storm, ends) in seen:
            continue
        seen.add(((curr_x, curr_y), curr_storm, ends))
        if time % 10 == 0 and time > currIncr:
            print((curr_x, curr_y), time, len(queue))
            currIncr = time
        if (curr_x, curr_y) == end:
            print(time)
            queue = [(end, curr_storm, time, ends + 1)]
            seen = set()
            break

        next_storm = set()
        storm_pos = set()
        if (time + 1) not in stormAtTime:
            for storm_x, storm_y, storm_dir in curr_storm:
                new_x = storm_x
                new_y = storm_y
                if storm_dir == '>':
                    new_x = storm_x + 1
                    new_y = storm_y
                    if (new_x, new_y) in walls:
                        new_x = 1
                        new_y = new_y
                elif storm_dir == '<':
                    new_x = storm_x - 1
                    new_y = storm_y
                    if (new_x, new_y) in walls:
                        new_x = farSide_x - 2
                        new_y = new_y
                elif storm_dir == 'v':
                    new_x = storm_x
                    new_y = storm_y + 1
                    if (new_x, new_y) in walls:
                        new_x = new_x
                        new_y = 1
                elif storm_dir == '^':
                    new_x = storm_x
                    new_y = storm_y - 1
                    if (new_x, new_y) in walls:
                        new_x = new_x
                        new_y = farSide_y - 2
                next_storm.add((new_x, new_y, storm_dir))
            stormAtTime[time + 1] = next_storm
        else:
            next_storm = stormAtTime[time + 1]
        for storm in next_storm:
            storm_pos.add((storm[0], storm[1]))

        consider_nexts = []
        for adjust_x, adjust_y in [(-1, 0), (0, -1), (1, 0), (0, 1), (0, 0)]:
            next_consider = (curr_x + adjust_x, curr_y + adjust_y)
            if next_consider not in storm_pos and next_consider not in walls:
                consider_nexts.append(next_consider)
        for next in consider_nexts:
            solid_storm = frozenset(next_storm)
            if (next, solid_storm, ends) not in seen:
                queue.append((next, solid_storm, time + 1, ends))