from pathlib import Path

path = Path(__file__)

f_in = f"{path.parent}/.in"

with open(f_in, "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

answer = 0

# Card   1: 34 50 18 44 19 35 47 62 65 26 | 63  6 27 15 60  9 98  3 61 89 31 43 80 37 54 49 92 55  8  7 10 16 52 33 45
for line in lines:
    card, game = line.split(": ")
    id = int(game.split()[-1])
    winning, numbers = game.split("|")
    winning = set(map(int, winning.split()))
    numbers = set(map(int, numbers.split()))
    n = len(winning.intersection(numbers))
    if n > 0:
        answer += 2 ** (n - 1)

print(answer)
