from pathlib import Path
from itertools import groupby

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = f.read()

res = [list(map(int, sub)) for _, sub in groupby(lines.split('\n'), key=bool) if _]
print(res)
answer = max(map(sum, res))

print(answer)
