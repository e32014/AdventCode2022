import re

file = open('input.txt')

totalScore = 1
pos = 0
for line in file:
    if pos >= 3:
        break
    bid, oreOre, clayOre, obsOre, obsClay, geoOre, geoObs = re.match("^Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.", line.strip()).groups()
    bid = int(bid)
    oreOre = int(oreOre)
    clayOre = int(clayOre)
    obsOre = int(obsOre)
    obsClay= int(obsClay)
    geoOre = int(geoOre)
    geoObs = int(geoObs)
    best = 0
    stack = [(0, 0, 0, 0, 32, 1, 0, 0, 0)]
    visited = set()
    while len(stack) > 0:
        ore, clay, obs, geode, time, bore, bclay, bobs, bgeode = stack.pop()
        best = max(best, geode)
        if time == 0:
            continue

        maxOre = max(oreOre, clayOre, obsOre, geoOre)
        if bore >= maxOre:
            bore = maxOre
        if bclay >= obsClay:
            bclay = obsClay
        if bobs >= geoObs:
            bobs = geoObs
        if ore >= time * maxOre - bore * (time - 1):
            ore = time * maxOre - bore * (time - 1)
        if clay >= time * obsClay - bclay * (time - 1):
            clay = time * obsClay - bclay * (time - 1)
        if obs >= time * geoObs - bobs * (time - 1):
            obs = time * geoObs - bobs * (time - 1)

        state = (ore, clay, obs, geode, time, bore, bclay, bobs, bgeode)
        if state in visited:
            continue
        visited.add(state)
        if len(visited) % 1000000 == 0:
            print(time, best, len(visited))
        stack.append((ore + bore, clay + bclay, obs + bobs, geode + bgeode, time - 1, bore, bclay, bobs, bgeode))
        if ore >= oreOre:
            stack.append((ore + bore - oreOre, clay + bclay, obs + bobs, geode + bgeode, time - 1, bore + 1, bclay, bobs, bgeode))
        if ore >= clayOre:
            stack.append((ore + bore - clayOre, clay + bclay, obs + bobs, geode + bgeode, time - 1, bore, bclay + 1, bobs, bgeode))
        if ore >= obsOre and clay >= obsClay:
            stack.append((ore + bore - obsOre, clay + bclay - obsClay, obs + bobs, geode + bgeode, time - 1, bore, bclay, bobs+1, bgeode))
        if ore >= geoOre and obs >= geoObs:
            stack.append((ore + bore - geoOre, clay + bclay, obs + bobs - geoObs, geode + bgeode, time - 1, bore, bclay, bobs, bgeode+1))
    print("Finished", bid, best)
    totalScore *= best
    pos += 1
print(totalScore)