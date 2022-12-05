import copy
import re

file = open('input.txt')

currLine = file.readline().strip('\n')
crates = []
while currLine != '':
    crates.append(currLine)
    currLine = file.readline().strip('\n')
print(crates)

stacks = [[] for i in range(0, int(crates[-1][-1]))]
for crate in crates[-2::-1]:
    print(crate)
    for i in range(0, len(crate), 4):
        box = crate[i + 1]
        if box != ' ':
            stacks[i//4].append(box)

masterStacks = copy.deepcopy(stacks)
currLine = file.readline().strip('\n')
while currLine != '':
    size, src, dest = [int(elem) for elem in re.match("move ([0-9]+) from ([0-9]+) to ([0-9]+)", currLine).groups()]
    currLine = file.readline().strip('\n')
    for _ in range(0, size):
        stacks[dest-1].append(stacks[src-1].pop())

    substack = []
    for _ in range(0, size):
        substack.append(masterStacks[src - 1].pop())
    substack.reverse()
    masterStacks[dest - 1] += substack

result = ""
masterResult = ""
for stack in stacks:
    result += stack[-1]
for stack in masterStacks:
    masterResult += stack [-1]

print(result)
print(masterResult)