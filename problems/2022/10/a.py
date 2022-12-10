from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = list(map(lambda x: x.split(), f.readlines()))

CYCLES = {20, 60, 100, 140, 180, 220}

signal_strength = 0
X = 1
cycle = 0

for line in lines:
    match line:
        case ["addx", V]:
            cycle += 1
            if cycle in CYCLES:
                signal_strength += X * cycle
            cycle += 1
            if cycle in CYCLES:
                signal_strength += X * cycle
            X += int(V)
        case ["noop"]:
            cycle += 1
            if cycle in CYCLES:
                signal_strength += X * cycle

print(signal_strength)
