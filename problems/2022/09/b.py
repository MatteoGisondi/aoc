from pathlib import Path

path = Path(__file__)

f_in = f'{path.parent}/.in'

DIR = {"U": (0, 1), "L": (-1, 0), "D": (0, -1), "R": (1, 0)}

with open(f_in, 'r') as f:
    lines = list(map(lambda x: x.split(), f.readlines()))

knots = [(0, 0)] * 10

visited = set()

for direction, distance in lines:
    movement = DIR[direction]
    for _ in range(int(distance)):
        knots[0] = (knots[0][0] + movement[0], knots[0][1] + movement[1])

        for i in range(1, len(knots)):
            x_H, y_H = knots[i - 1]
            x_T, y_T = knots[i]

            if abs(x_H - x_T) <= 1 and abs(y_H - y_T) <= 1:
                # no movement necessary
                pass
            elif x_H == x_T:
                # same direction
                if y_H > y_T:
                    y_T += 1
                else:
                    y_T -= 1
            elif y_H == y_T:
                # same direction
                if x_H > x_T:
                    x_T += 1
                else:
                    x_T -= 1
            else:
                # step diagonally
                if x_H > x_T:
                    x_T += 1
                else:
                    x_T -= 1
                if y_H > y_T:
                    y_T += 1
                else:
                    y_T -= 1

            knots[i] = (x_T, y_T)
        visited.add(knots[-1])

print(len(visited))
