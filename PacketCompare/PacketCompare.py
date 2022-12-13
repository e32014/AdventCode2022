import functools

file = open('input.txt')

def parsePacket(in_str, pos):
    if in_str[pos] == "[":
        packet = []
        pos += 1
        while in_str[pos] != "]":
            parsed, pos = parsePacket(in_str, pos)
            packet.append(parsed)
            if in_str[pos] != "]":
                pos += 1
        pos += 1
        return packet, pos
    else:
        val = ""
        while pos < len(in_str) and in_str[pos] not in [",", "]"]:
            val += in_str[pos]
            pos += 1
        return int(val), pos


def compareParsed(parsed1, parsed2):
    if parsed1 is None or parsed2 is None:
        return parsed1 is None, parsed2 is None and parsed1 is None
    elif isinstance(parsed1, int) and isinstance(parsed2, int):
        return parsed1 < parsed2, parsed1 == parsed2
    elif isinstance(parsed1, list) and isinstance(parsed2, list):
        isValid, equal = False, True
        i, j = 0, 0
        while equal:
            if i >= len(parsed1) or j >= len(parsed2):
                return i >= len(parsed1), j >= len(parsed2) and i >= len(parsed1)
            isValid, equal = compareParsed(parsed1[i], parsed2[j])
            i += 1
            j += 1
        return isValid, equal
    elif isinstance(parsed1, int):
        return compareParsed([parsed1], parsed2)
    elif isinstance(parsed2, int):
        return compareParsed(parsed1, [parsed2])


def comparison(input1, input2):
    val1, _ = parsePacket(input1, 0)
    val2, _ = parsePacket(input2, 0)
    comp, _ = compareParsed(val1, val2)
    if comp:
        return -1
    else:
        return 1


line = file.readline().strip()
messages = ["[[2]]", "[[6]]"]
while line != "":
    messages.append(line)
    line = file.readline().strip()
    messages.append(line)
    file.readline().strip()
    line = file.readline().strip()

messages.sort(key = functools.cmp_to_key(comparison))

print((messages.index("[[2]]") + 1) * (messages.index("[[6]]") + 1))