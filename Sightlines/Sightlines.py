file = open('input.txt')

grid = []
for line in file:
    grid.append([int(char) for char in line.strip()])

visible = 0
highestSeen = -1
for j in range(0, len(grid)):
    if j == 0 or j == len(grid) - 1:
        visible += len(grid[j])
        continue
    for i in range(0, len(grid[j])):
        if i == 0 or i == len(grid[j]) - 1:
            visible += 1
            continue
        score = 1
        look = j + 1
        while look < len(grid):
            if grid[j][i] <= grid[look][i]:
                look += 1
                break
            look += 1
        score *= abs(look - j) - 1
        look = j - 1
        while look >= 0:
            if grid[j][i] <= grid[look][i]:
                look -= 1
                break
            look -= 1

        score *= abs(look - j) - 1

        look = i + 1
        while look < len(grid[j]):
            if grid[j][i] <= grid[j][look]:
                look += 1
                break
            look += 1
        score *= abs(look - i) - 1
        look = i - 1
        while look >= 0:
            if grid[j][i] <= grid[j][look]:
                look -= 1
                break
            look -= 1
        score *= abs(look - i) - 1
        if score >= highestSeen:
            highestSeen = score
print(highestSeen)