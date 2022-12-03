file = open('input.txt')

sideA = set()
sideB = set()
scores = dict()
total = 0

bag = set()
currIntersect = set()
bagNum = 0
badgeTotal = 0

for i in range(26):
    scores[chr(97+i)] = i + 1
    scores[chr(65 + i)] = i + 27

for line in file:
    if bagNum == 0:
        bag = set(line.strip())
        currIntersect = bag
        bagNum += 1
    elif bagNum == 1:
        bag = set(line.strip())
        currIntersect = currIntersect.intersection(bag)
        bagNum += 1
    else:
        bag = set(line.strip())
        currIntersect = currIntersect.intersection(bag)
        for elem in currIntersect:
            badgeTotal += scores[elem]
        bagNum = 0
        currIntersect = set()

    sideA = set(line.strip()[0:len(line.strip())//2])
    sideB = set(line.strip()[len(line.strip())//2:])
    for elem in sideA.intersection(sideB):
        total += scores[elem]
print(total)
print(badgeTotal)