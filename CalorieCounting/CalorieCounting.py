file = open('input.txt')

elves = []

elf = (0, [])
maxElf = 0
for line in file:
    if line == '\n':
        if elf[0] > maxElf:
            maxElf = elf[0]
        elves.append(elf)
        elf = (0, [])
    else:
        elf = (elf[0] + int(line.strip()), elf[1] + [int(line.strip())])

print(maxElf)
elves.sort(key=lambda x:x[0])
print(sum(elf[0] for elf in elves[-3:]))