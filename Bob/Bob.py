file = open('input.txt')

sum = 0
for line in file:
    number = list(line.strip())
    converted = 0
    factor = 0
    for i in range(len(number)-1, -1, -1):
        if number[i] == '2':
            converted += 2 * (5 ** factor)
        elif number[i] == '1':
            converted += 1 * (5 ** factor)
        elif number[i] == '-':
            converted += -1 * (5 ** factor)
        elif number[i] == '=':
            converted += -2 * (5 ** factor)
        factor += 1
    print(number, converted)
    sum += converted
print(sum)

chars = ['=', '-', '0', '1', '2']
result = ''
while sum > 0:
    n = (sum + 2) % 5
    sum = (sum + 2) // 5
    result = chars[n] + result
print(result)