from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/{path.stem}.in'

with open(f_in, 'r') as f:
    lines = list(map(int, f.readlines()))

answer = 0

for line in lines:
    pass

print(answer)
