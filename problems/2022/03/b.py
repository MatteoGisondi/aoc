from pathlib import Path

import multiset

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = f.readlines()

answer = 0

for i, line in enumerate(lines[::3]):
    a, b, d = [multiset.Multiset(l.strip()) for l in lines[i*3:i*3+3]]
    c = list(multiset.Multiset.intersection(a, b, d).items())[0][0]
    if (o := ord(c)) > 95:
        v = o - 96
    else:
        v = o - 38
    answer += v

print(answer)
