file = open('input.txt')

decrypt = 811589153
class linkedObj():
    def __init__(self, left, right, value):
        self.left = left
        self.right = right,
        self.value = value

    def __str__(self):
        return self.value


def printRing(front):
    print(front.value, end=" ")
    curr = front.right
    while curr != front:
        print(curr.value, end = " ")
        curr = curr.right
    print()


ring = []
front = None
for line in file:
    if len(ring) == 0:
        ring.append(linkedObj(None, None, int(line.strip()) * decrypt))
    else:
        ring.append(linkedObj(ring[-1], None, int(line.strip()) * decrypt))
        ring[-2].right = ring[-1]
    if ring[-1].value == 0:
        front = ring[-1]

ring[-1].right = ring[0]
ring[0].left = ring[-1]

for _ in range(10):
    count = 0
    for node in ring:
        target = node
        move = node.value % (len(ring) - 1)
        for _ in range(move):
            target = target.right
        if node.value != 0:
            node.right.left, node.left.right = node.left, node.right
            node.right, target.right.left = target.right, node
            node.left = target
            target.right = node
        if count % 100 == 0:
            print(count)
        count += 1

total = 0
curr = front
for i in range(0, 3000):
    curr = curr.right
    if i % 1000 == 999:
        total += curr.value
        print(curr.value)

print(total)