from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    lines = map(int, f.readlines())

def get_fuel(fuel):
    fuel = fuel // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + get_fuel(fuel)

answer = sum(get_fuel(line) for line in lines)

print(answer)
