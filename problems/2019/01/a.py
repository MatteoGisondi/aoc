from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = map(int, f.readlines())

answer = sum(line // 3 - 2 for line in lines)

print(answer)
