import re

file = open('input.txt')

map = dict()
usefulValves = set()
for line in file:
    groups = re.match("^Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? ((?:[A-Z]+(?:, )?)+)", line.strip()).groups()
    nexts = groups[2].split(", ")
    nexts.reverse()
    map[groups[0]] = (int(groups[1]), nexts)
    if int(groups[1]) > 0:
        usefulValves.add(groups[0])

start = ("AA", "AA", 0, 26, 0, set())
queue = [start]
visited = dict()
finished = []
maxi = 0
while len(queue) > 0:
    curr_pos, ele_pos, total_release, time, curr_rate, opened = queue.pop()
    visited[time, curr_pos, ele_pos] = total_release
    if time == 0:
        finished.append((curr_pos, ele_pos, total_release, time, curr_rate, opened))
        maxi = max(maxi, total_release)
        print(maxi)
        continue
    curr_open = map[curr_pos][0] > 0 and curr_pos not in opened
    ele_open = map[ele_pos][0] > 0 and ele_pos not in opened
    ele_moves = []
    if ele_pos != curr_pos and ele_open:
        ele_moves.append((ele_pos, True))
    for next_pos in map[ele_pos][1]:
        ele_moves.append((next_pos, False))

    if map[curr_pos][0] > 0 and curr_pos not in opened:
        for new_ele_pos, ele_open in ele_moves:
            new_rate = curr_rate + map[curr_pos][0]
            new_set = set()
            new_set.add(curr_pos)
            if ele_open:
                new_rate += map[new_ele_pos][0]
                new_set.add(new_ele_pos)
            if visited.get((time - 1, curr_pos, new_ele_pos), -1) < total_release + new_rate:
                queue.append((curr_pos, new_ele_pos, total_release + curr_rate, time - 1, new_rate, opened.union(new_set)))
    if any([val not in opened for val in usefulValves]):
        for next_pos in map[curr_pos][1]:
            for new_ele_pos, ele_open in ele_moves:
                new_rate = curr_rate
                new_set = set()
                if ele_open:
                    new_rate += map[new_ele_pos][0]
                    new_set.add(new_ele_pos)
                if visited.get((time - 1, next_pos, new_ele_pos), -1) < total_release + new_rate:
                    queue.append((next_pos, new_ele_pos, total_release + curr_rate, time - 1, new_rate, opened.union(new_set)))
    else:
        queue.append((curr_pos, ele_pos, total_release + (curr_rate * time), 0, curr_rate, opened))
finished.sort(key=lambda x: x[2], reverse=True)
print(finished[0])