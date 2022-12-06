file = open('input.txt')

stream = file.readline().strip()

chars = set()
for i in range(3, len(stream)):
    chars.add(stream[i])
    chars.add(stream[i - 1])
    chars.add(stream[i - 2])
    chars.add(stream[i - 3])
    if len(chars) == 4:
        print(i+1)
        break
    chars = set()

chars = set()
for i in range(13, len(stream)):
    for j in range(14):
        if stream[i - j] in chars:
            break
        chars.add(stream[i - j])
    if len(chars) == 14:
        print(i+1)
        break
    chars = set()