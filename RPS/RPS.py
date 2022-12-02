file = open("input.txt")

myScore = 0
winScore = 0

scoreMat = {'A': {'X': 4, 'Y': 8, 'Z': 3}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 7, 'Y': 2, 'Z': 6}}
winMat = {'A': {'X': 3, 'Y': 4, 'Z': 8}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 2, 'Y': 6, 'Z': 7}}

for line in file:
    opp, me = line.strip().split()
    myScore += scoreMat[opp][me]
    winScore += winMat[opp][me]

print(myScore)
print(winScore)