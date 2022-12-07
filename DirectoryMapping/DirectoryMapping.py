file = open('input.txt')

class File:
    def __init__(self, name):
        self.parent = None
        self.name = name
        self.children = {}
        self.size = 0

rootDirectory = File("/")
currDirectory = rootDirectory
line = file.readline().strip()
directories = [rootDirectory]
while line != '':
    if line.startswith("$"):
        args = line.split()
        if args[1] == 'cd':
            if args[2] == '/':
                currDirectory = rootDirectory
            elif args[2] == '..':
                currDirectory = currDirectory.parent
            else:
                currDirectory = currDirectory.children[args[2]]
            line = file.readline().strip()
        elif args[1] == 'ls':
            line = file.readline().strip()
            while line != '' and not line.startswith("$"):
                typer, name = line.split()
                currFile = File(name)
                currFile.parent = currDirectory
                currDirectory.children[name] = currFile
                if typer != 'dir':
                    currFile.size = int(typer)
                else:
                    directories.append(currFile)
                line = file.readline().strip()


def recSum(directory):
    sum = 0
    if directory.size != 0:
        return
    for child in directory.children.values():
        recSum(child)
        sum += child.size
    directory.size = sum


recSum(rootDirectory)
smallDirTotal = 0
for directory in directories:
    if directory.size < 100_000:
        smallDirTotal += directory.size
print(smallDirTotal)

total = 70_000_000
goal = 30_000_000
curr = rootDirectory.size
directories.sort(key= lambda dir: dir.size)
for directory in directories:
    if curr - directory.size < total - goal:
        print(directory.size)
        break