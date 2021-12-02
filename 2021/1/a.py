from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/{path.stem}.in'

with open(f_in, 'r') as f:
    lines = list(map(int, f.readlines()))

n_greater = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        n_greater += 1

print(n_greater)
