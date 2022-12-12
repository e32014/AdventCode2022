file = open('input.txt')

def findNext(map, pos):
    next = []
    currOrd = ord(map[pos[1]][pos[0]])
    if pos[0] - 1 >= 0 and ord(map[pos[1]][pos[0] - 1]) - currOrd <= 1:
        next.append((pos[0] - 1, pos[1]))
    if pos[1] - 1 >= 0 and ord(map[pos[1] - 1][pos[0]]) - currOrd <= 1:
        next.append((pos[0], pos[1] - 1))
    if pos[0] + 1 < len(map[pos[1]]) and ord(map[pos[1]][pos[0] + 1]) - currOrd <= 1:
        next.append((pos[0] + 1, pos[1]))
    if pos[1] + 1 < len(map) and ord(map[pos[1] + 1][pos[0]]) - currOrd <= 1:
        next.append((pos[0], pos[1] + 1))
    return next


map = []
starts = []
end = (0, 0)
for line in file:
    map.append(list(line.strip()))
    for i in range(len(line.strip())):
        if 'S' == line[i] or 'a' == line[i]:
            starts.append((i, len(map) - 1))
            map[-1][i] = 'a'
    if 'E' in line:
        end = (line.find('E'), len(map) - 1 )
        map[end[1]][end[0]] = 'z'

prev = dict()
for start in starts:
    prev[start] = None
queue = [] + starts
curr = queue.pop(0)
while curr != end:
    moves = findNext(map, curr)
    for move in moves:
        if move not in prev:
            prev[move] = curr
            queue.append(move)
    curr = queue.pop(0)

count = 0
while curr not in starts:
    curr = prev[curr]
    count += 1
print(count)