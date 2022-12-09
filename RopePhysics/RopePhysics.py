file = open('input.txt')


def move(pos, direct):
    if direct == 'U':
        return pos[0], pos[1] + 1
    elif direct == 'L':
        return pos[0] - 1, pos[1]
    elif direct == 'R':
        return pos[0] + 1, pos[1]
    elif direct == 'D':
        return pos[0], pos[1] - 1


def next_to(target, looker):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if target[0] == looker[0] + i and target[1] == looker[1] + j:
                return True
    return False


def move_plan(target, looker):
    x_plan = target[0] - looker[0]
    y_plan = target[1] - looker[1]
    plan = ""
    if x_plan > 0:
        plan += "R"
    elif x_plan < 0:
        plan += "L"
    if y_plan > 0:
        plan += "U"
    elif y_plan < 0:
        plan += "D"
    return plan


rope = [(0, 0) for i in range(10)]

tailPoses = set()
tailPoses.add(rope[-1])

for command in file:
    direct, dist = command.strip().split()
    dist = int(dist)
    for _ in range(dist):
        rope[0] = move(rope[0], direct)
        for i in range(1, len(rope)):
            if not next_to(rope[i - 1], rope[i]):
                plan = move_plan(rope[i - 1], rope[i])
                for step in plan:
                    rope[i] = move(rope[i], step)
        tailPoses.add(rope[-1])

print(len(tailPoses))