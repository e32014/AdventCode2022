file = open('input.txt')

def monkeySolver(monkeyId, monkeyMap, monkeyTracker):
    if monkeyId in monkeyTracker:
        return monkeyTracker[monkeyId]
    monkeyMath = monkeyMap[monkeyId]
    if isinstance(monkeyMath, int):
        monkeyTracker[monkeyId] = monkeyMath
    elif monkeyId == 'humn':
        monkeyTracker[monkeyId] = 'humn'
    else:
        monkeyId1, monkeyOp, monkeyId2 = monkeyMath
        monkeyVal1 = monkeySolver(monkeyId1, monkeyMap, monkeyTracker)
        monkeyVal2 = monkeySolver(monkeyId2, monkeyMap, monkeyTracker)
        if isinstance(monkeyVal1, int) and isinstance(monkeyVal2, int):
            if monkeyOp == '+':
                monkeyTracker[monkeyId] = monkeyVal1 + monkeyVal2
            elif monkeyOp == '-':
                monkeyTracker[monkeyId] = monkeyVal1 - monkeyVal2
            elif monkeyOp == '*':
                monkeyTracker[monkeyId] = monkeyVal1 * monkeyVal2
            elif monkeyOp == '/':
                monkeyTracker[monkeyId] = monkeyVal1 // monkeyVal2
            elif monkeyOp == '=':
                monkeyTracker[monkeyId] = [monkeyVal1 if isinstance(monkeyVal1, int) else monkeyId1, monkeyOp, monkeyVal2 if isinstance(monkeyVal2, int) else monkeyId2]
        else:
            monkeyTracker[monkeyId] = [monkeyVal1 if isinstance(monkeyVal1, int) else monkeyId1, monkeyOp, monkeyVal2 if isinstance(monkeyVal2, int) else monkeyId2]
    return monkeyTracker[monkeyId]

monkeyMap = dict()
for line in file:
    monkeyId, monkeyMath = line.strip().split(':')
    monkeyMath = monkeyMath.split()
    if monkeyId == 'root':
        monkeyMath[1] = '='
    monkeyMap[monkeyId] = int(monkeyMath[0]) if len(monkeyMath) == 1 else monkeyMath
    if monkeyId == 'humn':
        monkeyMap[monkeyId] = 'humn'

print(monkeyMap)
monkeyTracker = dict()
monkeySolver('root', monkeyMap, monkeyTracker)
print(monkeyTracker)

curr = 'root'
val = 0
while curr != 'humn':
    monkeyLeft, monkeyOp, monkeyRight = monkeyTracker[curr]
    onLeft = not isinstance(monkeyLeft, int)
    onRight = not isinstance(monkeyRight, int)
    if monkeyOp == '=':
        if onLeft:
            curr = monkeyLeft
            val = monkeyRight
        elif onRight:
            curr = monkeyRight
            val = monkeyLeft
    elif monkeyOp == '+':
        if onLeft:
            curr = monkeyLeft
            val -= monkeyRight
        elif onRight:
            curr = monkeyRight
            val -= monkeyLeft
    elif monkeyOp == '-':
        if onLeft:
            curr = monkeyLeft
            val += monkeyRight
        elif onRight:
            curr = monkeyRight
            val = -(val - monkeyLeft)
    elif monkeyOp == '*':
        if onLeft:
            curr = monkeyLeft
            val = val // monkeyRight
        elif onRight:
            curr = monkeyRight
            val = val // monkeyLeft
    elif monkeyOp == '/':
        if onLeft:
            curr = monkeyLeft
            val = val * monkeyRight
        elif onRight:
            print("HATE")
            curr = monkeyRight
            val = monkeyLeft // val
print(val)