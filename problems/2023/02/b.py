from pathlib import Path

path = Path(__file__)

f_in = f"{path.parent}/.in"

with open(f_in, "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

answer = 0


# Game 1: 8 green; 5 green, 6 blue, 1 red; 2 green, 1 blue, 4 red; 10 green, 1 red, 2 blue; 2 blue, 3 red
for line in lines:
    game, bags = line.split(": ")
    id = int(game.split()[-1])
    counts = {"red": 0, "green": 0, "blue": 0}
    for bag in bags.split("; "):
        for block in bag.split(", "):
            n, color = block.split()
            if counts[color] < int(n):
                counts[color] = int(n)
    answer += counts["red"] * counts["green"] * counts["blue"]

print(answer)
