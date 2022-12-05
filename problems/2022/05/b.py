from pathlib import Path
from collections import deque
from re import *

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = f.readlines()
    crates, actions = lines[:9], lines[10:]

crate_slices = [_.replace("] ", "]-").replace("    ", ". ").replace("]-", "] ").split() for _ in crates[:-1]]

crate_stacks = [deque() for _ in crates[-1].split()]

for s in crate_slices[::-1]:
    for i, crate in enumerate(s):
        if crate != ".":
            crate_stacks[i].append(crate.replace("[", "").replace("]", ""))

print(*enumerate(crate_stacks, start=1), sep="\n")

print()

for action in actions:
    print(action)
    p = action.split()
    n, f, t = map(int, (p[1], p[3], p[5]))
    # print(f"{crate_stacks[f - 1]=}")
    moved = deque(crate_stacks[f - 1].pop() for _ in range(n))
    print(f"{moved=}")
    while moved:
        crate_stacks[t - 1].append(moved.pop())
    # print(f"{crate_stacks[t - 1]=}")
    print(*enumerate(crate_stacks, start=1), sep="\n")

print("".join(list(stack[-1] for stack in crate_stacks)))
