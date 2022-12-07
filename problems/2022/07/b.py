from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = list(map(lambda x: x.split(), f.readlines()))

answer = 0

class ParentDict(dict):
    def __init__(self, parent):
        self.parent = parent
        self.size = 0

    def add(self, size):
        self.size += size
        parent = self.parent
        while parent is not None:
            parent.size += size
            parent = parent.parent

file_structure = {}
cwd = file_structure["/"] = ParentDict(None)
total_size = 0

for i, line in enumerate(lines[1:], start=2):
    match line:
        case ["$", "cd", directory]:
            if directory == "..":
                cwd = cwd.parent
            else:
                cwd = ParentDict(cwd)
                cwd.parent[directory] = cwd
        case ["$", "ls"]:
            pass
        case ["dir", directory]:
            cwd[directory] = ParentDict(cwd)
        case [size, file]:
            cwd[file] = int(size)
            cwd.add(int(size))

answer = file_structure["/"].size

min_space = answer - 70000000 + 30000000

def candidate(directory):
    global answer
    for child in directory.values():
        if isinstance(child, ParentDict):
            if child.size >= min_space:
                if child.size < answer:
                    answer = child.size
                candidate(child)

candidate(file_structure)

print(answer)
