from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = f.readlines()

answer = 0

for line in lines:
    s = line.strip()
    l = len(s) // 2
    a, b = set(s[:l]), set(s[l:])

    for c in a:
        if c in b:
            print(c)
            if (o := ord(c)) > 95:
                v = o - 96
                answer += v
            else:
                v = o - 38
                answer += v
            break

print(answer)
