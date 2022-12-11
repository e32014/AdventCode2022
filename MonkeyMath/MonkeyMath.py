import re

file = open('input.txt')


class Monkey:
    def __init__(self):
        self.items = []
        self.id = 0
        self.operation = ['+', '0', '0']
        self.test = 1
        self.onTrue = -1
        self.onFalse = -1
        self.inspects = 0

    def operate(self, item):
        self.inspects += 1
        left = item if self.operation[1] == 'old' else int(self.operation[1])
        right = item if self.operation[2] == 'old' else int(self.operation[2])
        if self.operation[0] == '+':
            return left + right
        elif self.operation[0] == '*':
            return left * right


monkeys = {}
title = file.readline().strip()
commonTest = 1
while title != "":
    id = int(title.split()[1][:-1])
    currMonkey = Monkey()
    currMonkey.id = id
    monkeys[id] = currMonkey
    startsWith = [int(val.replace(",", "")) for val in file.readline().strip().split()[2:]]
    currMonkey.items = startsWith
    op = file.readline().strip().split()[3:]
    currMonkey.operation = [op[1], op[0], op[2]]
    currMonkey.test = int(file.readline().strip().split()[3])
    commonTest *= currMonkey.test
    currMonkey.onTrue = int(file.readline().strip().split()[5])
    currMonkey.onFalse = int(file.readline().strip().split()[5])
    file.readline()
    title = file.readline().strip()


steps = 10000
for _ in range(steps):
    for i in range(len(monkeys)):
        for item in monkeys[i].items:
            worry = monkeys[i].operate(item) % commonTest
            if worry % monkeys[i].test == 0:
                monkeys[monkeys[i].onTrue].items.append(worry)
            else:
                monkeys[monkeys[i].onFalse].items.append(worry)
        monkeys[i].items = []

for monkey in monkeys.values():
    print(monkey.id, monkey.items, monkey.operation, monkey.test, monkey.onTrue, monkey.onFalse, monkey.inspects)

slist = sorted(monkeys.values(), key= lambda x:x.inspects)
print(slist[-1].inspects * slist[-2].inspects)