from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/{path.stem}.in'

with open(f_in, 'r') as f:
    lines = list(map(int, f.readlines()))

n_greater = 0
depths = []
for i in range(len(lines) - 2):
    depths.append(lines[i] + lines[i + 1] + lines[i + 2])
    if i > 0:
        if depths[i] > depths[i - 1]:
            n_greater += 1

print(n_greater)
