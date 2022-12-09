from pathlib import Path
import itertools

path = Path(__file__)

f_in = f'{path.parent}/.in'

DIR = {"U": (0, 1), "L": (-1, 0), "D": (0, -1), "R": (1, 0)}

with open(f_in, 'r') as f:
    lines = list(map(lambda x: x.split(), f.readlines()))

x_H, y_H = 0, 0
x_T, y_T = 0, 0

visited = set()

for direction, distance in lines:
    movement = DIR[direction]
    for _ in range(int(distance)):
        x_H += movement[0]
        y_H += movement[1]

        if x_T - x_H == 2:
            if y_T != y_H:
                y_T = y_H
            x_T -= 1
        elif x_H - x_T == 2:
            if y_T != y_H:
                y_T = y_H
            x_T += 1

        if y_T - y_H == 2:
            if x_T != x_H:
                x_T = x_H
            y_T -= 1
        elif y_H - y_T == 2:
            if x_T != x_H:
                x_T = x_H
            y_T += 1

        visited.add((x_T, y_T))

print(len(visited))
