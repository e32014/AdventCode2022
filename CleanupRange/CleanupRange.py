import re

file = open("input.txt")

fullcount = 0
anycount = 0
for line in file:
    min1, max1, min2, max2 = [int(elem) for elem in re.split("[,-]", line.strip())]
    if min1 >= min2 and max1 <= max2:
        fullcount += 1
    elif min2 >= min1 and max2 <= max1:
        fullcount += 1

    if max1 >= max2 >= min1 or max1 >= min2 >= min1 or max2 >= max1 >= min2 or max2 >= min1 >= min2:
        anycount += 1

print(fullcount)
print(anycount)