from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

chart = {
    "B X": 1,
    "C Y": 2,
    "A Z": 3,
    "A X": 4,
    "B Y": 5,
    "C Z": 6,
    "C X": 7,
    "A Y": 8,
    "B Z": 9,
}

convert = {
    "B X": "B X",
    "C Y": "C Z",
    "A Z": "A Y",
    "A X": "A Z",
    "B Y": "B Y",
    "C Z": "C X",
    "C X": "C Y",
    "A Y": "A X",
    "B Z": "B Z",
}

with open(f_in, 'r') as f:
    lines = f.readlines()

answer = sum(chart[convert[line.strip()]] for line in lines)

print(answer)
