from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

chart = {
    "B X": 1, # 0 + 1
    "C Y": 2, # 0 + 2
    "A Z": 3, # 0 + 3
    "A X": 4, # 3 + 1
    "B Y": 5, # 3 + 2
    "C Z": 6, # 3 + 3
    "C X": 7, # 6 + 1
    "A Y": 8, # 6 + 2
    "B Z": 9, # 6 + 3
}

with open(f_in, 'r') as f:
    lines = f.readlines()

answer = sum(chart[line.strip()] for line in lines)

print(answer)
