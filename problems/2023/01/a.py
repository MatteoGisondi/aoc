from pathlib import Path

path = Path(__file__)

f_in = f"{path.parent}/.in"

with open(f_in, "r") as f:
    lines = list(f.readlines())

answer = 0


def find_digit(iterable):
    for i in iterable:
        if i.isnumeric():
            return i


for line in lines:
    l_int = find_digit(line)
    r_int = find_digit(reversed(line))
    answer += int(l_int + r_int)

print(answer)
