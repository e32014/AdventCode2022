file = open('input.txt')

board = []
tops = []
bottoms = []
lefts = []

line = file.readline()
trueWidth = 0
while line.strip('\n') != '':
    board.append(list(line[:-1]))
    trueWidth = max(len(board[-1]), trueWidth)
    if '#' in board[-1]:
        lefts.append(min(board[-1].index('.'), board[-1].index('#')))
    else:
        lefts.append(board[-1].index('.'))
    line = file.readline()

commands = file.readline().strip()

print(lefts)

for i in range(trueWidth):
    unseen = True
    bottom = 0
    for j in range(len(board)):
        if len(board[j]) <= i:
            continue
        if board[j][i] == '.' or board[j][i] == '#':
            if unseen:
                tops.append(j)
                unseen = False
            bottom = j
        if not unseen and board[j][i] == ' ':
            bottoms.append(bottom)
            unseen = True
            break
    if not unseen:
        bottoms.append(bottom)

print(tops)
print(bottoms)
pos = (lefts[0], 0, 0)

while len(commands) > 0:
    command = ''
    while len(commands) > 0 and commands[0] != 'R' and commands[0] != 'L':
        command += commands[0]
        commands = commands[1:]
    if command == '':
        command = commands[0]
        commands = commands[1:]

    if command == 'R':
        pos = (pos[0], pos[1], (5 + pos[2]) % 4)
    elif command == 'L':
        pos = (pos[0], pos[1], (3 + pos[2]) % 4)
    else:
        command = int(command)
        for _ in range(command):
            con_x, con_y, con_dir = pos
            if con_dir == 0:
                con_x += 1
            elif con_dir == 1:
                con_y += 1
            elif con_dir == 2:
                con_x -= 1
            elif con_dir == 3:
                con_y -= 1
            if con_dir == 1 and con_y > bottoms[con_x]:
                if con_y == 200:
                    # 1 to 6
                    con_x = con_x + 100
                    con_y = 0
                elif con_y == 150:
                    # 3 to 1
                    con_y = con_x + 100
                    con_x = 49
                    con_dir = 2
                elif con_y == 50:
                    # 6 to 4
                    con_dir = 2
                    con_y = con_x - 50
                    con_x = 99
            elif con_dir == 3 and con_y < tops[con_x]:
                if con_y == 99:
                    # 2 to 4
                    con_y = con_x + 50
                    con_x = 50
                    con_dir = 0
                elif con_y == -1 and con_x < 100:
                    # 5 to 1
                    con_dir = 0
                    con_y = con_x + 100
                    con_x = 0
                elif con_y == -1 and con_x >= 100:
                    # 6 to 1
                    con_x = con_x - 100
                    con_y = 199
            elif con_dir == 0 and con_x > len(board[con_y]) - 1:
                if con_x == 50:
                    # 1 to 3
                    con_dir = 3
                    con_x = con_y - 100
                    con_y = 149
                elif con_x == 100 and con_y >= 100:
                    #inverted
                    # 3 to 6
                    con_dir = 2
                    con_y = (149 - con_y)
                    con_x = 149
                elif con_x == 100 and con_y < 100:
                    # 4 to 6
                    con_dir = 3
                    con_x = con_y + 50
                    con_y = 49
                elif con_x == 150:
                    #inverted
                    # 6 to 3
                    con_dir = 2
                    con_y = (49 - con_y) + 100
                    con_x = 99
            elif con_dir == 2 and con_x < lefts[con_y]:
                if con_x == -1 and con_y >= 150:
                    # 1 to 5
                    con_dir = 1
                    con_x = con_y - 100
                    con_y = 0
                elif con_x == -1 and con_y < 150:
                    #inverted
                    # 2 to 5
                    con_dir = 0
                    con_y = (149 - con_y)
                    con_x = 50
                elif con_x == 49 and con_y >= 50:
                    # 4 to 2
                    con_dir = 1
                    con_x = con_y - 50
                    con_y = 100
                elif con_x == 49 and con_y < 50:
                    #inverted
                    # 5 to 2
                    con_dir = 0
                    con_y = (49 - con_y) + 100
                    con_x = 0
            if board[con_y][con_x] == '#':
                break
            pos = (con_x, con_y, con_dir)
    print(command, pos)
print(pos)
print((pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + pos[2])