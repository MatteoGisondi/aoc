from pathlib import Path

path = Path(__file__)

f_in = f"{path.parent}/.in"

with open(f_in, "r") as f:
    lines = [l.strip() for l in f.readlines()]


NUMS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first(line):
    if (l := len(line)) < 3:
        for c in line:
            if c.isnumeric():
                return c
    for i in range(l - 2):
        if (c := line[i]).isnumeric():
            return c
        for j in range(3, 6):
            if num := NUMS.get(line[i : i + j]):
                return num
    for c in line[-3:]:
        if c.isnumeric():
            return c


def get_last(line):
    if (l := len(line)) < 3:
        for c in line[::-1]:
            if c.isnumeric():
                return c
    for c in line[-1:-3:-1]:
        if c.isnumeric():
            return c
    for i in range(l - 3, 0, -1):
        if (c := line[i]).isnumeric():
            return c
        for j in range(3, 6):
            if num := NUMS.get(line[i : i + j]):
                return num
    for c in line[-3::-1]:
        if c.isnumeric():
            return c


answer = 0

for line in lines:
    l_int = get_first(line)
    r_int = get_last(line)
    answer += int(l_int + r_int)

print(answer)
