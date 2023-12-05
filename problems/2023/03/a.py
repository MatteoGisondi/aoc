from pathlib import Path

path = Path(__file__)

f_in = f"{path.parent}/.in"

with open(f_in, "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

N, M = len(lines), len(lines[0])

answer = 0


def get_part(i, j):
    l = []
    while i > 0 and lines[j][i - 1].isnumeric():
        i -= 1
    while i < M and (c := lines[j][i]).isnumeric():
        l.append(c)
        i += 1
    part = int("".join(l))
    return part


# no symbols on edges
for j, line in enumerate(lines[1:-1], start=1):
    for i, c in enumerate(line[1:-1], start=1):
        if c == ".":
            continue
        if not c.isalnum():
            # check sides
            for di, dj in [(-1, 0), (1, 0)]:
                if lines[j + dj][i + di].isnumeric():
                    answer += get_part(i + di, j + dj)
            # check top
            top = False
            for di, dj in [(0, -1)]:
                if lines[j + dj][i + di].isnumeric():
                    answer += get_part(i + di, j + dj)
                    top = True
            # check top corners
            if not top:
                for di, dj in [(-1, -1), (1, -1)]:
                    if lines[j + dj][i + di].isnumeric():
                        answer += get_part(i + di, j + dj)
            # check bottom
            bottom = False
            for di, dj in [(0, 1)]:
                if lines[j + dj][i + di].isnumeric():
                    answer += get_part(i + di, j + dj)
                    bottom = True
            # check bottom corners
            if not bottom:
                for di, dj in [(-1, 1), (1, 1)]:
                    if lines[j + dj][i + di].isnumeric():
                        answer += get_part(i + di, j + dj)
print(answer)
