file = open('input.txt')
droplets = set()

def gen_adj(pos):
    x, y, z = pos
    adj = []
    for i in range(-1, 2):
        adj.append((x + i, y, z))
    for j in range(-1, 2):
        adj.append((x, y + j, z))
    for k in range(-1, 2):
        adj.append((x, y, z + k))
    return adj


for line in file:
    droplets.add(tuple([int(val) for val in line.strip().split(",")]))

surface = set()
maxX, maxY, maxZ = [-100000000 for _ in range(3)]
minX, minY, minZ = [100000000 for _ in range(3)]
shares = dict()
for droplet in droplets:
    x, y, z = droplet
    if x > maxX:
        maxX = x
    if x < minX:
        minX = x
    if y > maxY:
        maxY = y
    if y < minY:
        minY = y
    if z > maxZ:
        maxZ = z
    if z < minZ:
        minZ = z
    adjs = gen_adj(droplet)
    for adj in adjs:
        if adj not in droplets:
            surface.add(adj)
            shares[adj] = shares.get(adj, 0) + 1
total = 0
for air in surface:
    total += shares[air]
print(total)
outside = set()
inside = set()
for air in surface:
    if air in outside or air in inside:
        continue
    nexts = [air]
    isOutside = False
    seen = set()
    while len(nexts) != 0:
        next = nexts.pop(0)
        x, y, z = next
        seen.add(next)
        if x > maxX or x < minX or y > maxY or y < minY or z > maxZ or z < minZ:
            isOutside = True
            break
        if next in outside:
            isOutside = True
            break
        elif next in inside:
            break
        adjs = gen_adj(next)
        for adj in adjs:
            if adj not in droplets and adj not in nexts and adj not in seen:
                nexts.append(adj)
    if not isOutside:
        inside = inside.union(seen.intersection(surface))
    else:
        outside = outside.union(seen.intersection(surface))
total = 0
for air in outside:
    total += shares[air]
print(total)