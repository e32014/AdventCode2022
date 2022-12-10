file = open('input.txt')

nums = []
crt = ["." for i in range(0, 241)]
cycles = 1

command = file.readline().strip()
register = 1
screenPos = 1
hold = False
holdVal = None
while command != "":
    if -1 <= (register + 1 - screenPos) <= 1:
        crt[cycles] = "█"
    if screenPos == 40:
        screenPos = 0
    if (cycles - 20) % 40 == 0:
        nums.append(register * cycles)
    if cycles == 240:
        break
    if hold:
        register += holdVal
        hold = False
    else:
        if command.startswith("addx"):
            comm, val = command.split()
            hold = True
            holdVal = int(val)
        command = file.readline().strip()
    cycles += 1
    screenPos += 1

print(sum(nums[0:6]))

for i in range(1, len(crt)):
    print(crt[i], end="")
    if i % 40 == 0:
        print()