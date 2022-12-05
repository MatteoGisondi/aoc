from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = list(map(lambda x: x.strip().split(","), f.readlines()))

answer = 0

for line in lines:
    a, b = map(lambda x: x.split("-"), line)
    a1, a2 = map(int, a)
    b1, b2 = map(int, b)

    if (a1 <= b1) and (a2 >= b2):
        answer += 1
        print("a contains b")
        print(a, b)
    elif (b1 <= a1) and (b2 >= a2):
        answer += 1
        print("b contains a")
        print(b, a)

print(answer)
