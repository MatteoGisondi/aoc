from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = list(map(lambda x: x.split(), f.readlines()))

signal_strength = 0
X = 1
cycle = 0

CRT = [[], [], [], [], [], []]

for line in lines:
    match line:
        case ["addx", V]:
            d, r = divmod(cycle, 40)
            if X - 1 <= r <= X + 1:
                CRT[d].append("#")
            else:
                CRT[d].append(".")
            cycle += 1
            d, r = divmod(cycle, 40)
            if X - 1 <= r <= X + 1:
                CRT[d].append("#")
            else:
                CRT[d].append(".")
            cycle += 1
            X += int(V)
        case ["noop"]:
            d, r = divmod(cycle, 40)
            if X - 1 <= r <= X + 1:
                CRT[d].append("#")
            else:
                CRT[d].append(".")
            cycle += 1

print("\n".join("".join(_) for _ in CRT), sep="\n")
