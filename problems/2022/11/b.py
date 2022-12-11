from pathlib import Path
from collections import deque

path = Path(__file__)

f_in = f'{path.parent}/.in'

divisor = 1

class Monkey():
    def __init__(self, body):
        id = body[0].split()[-1].strip(":")
        starting_items = body[1].split(": ")[-1]
        operation = body[2].split(": ")[-1]
        test = body[3].split(": ")[-1]
        if_true, if_false = body[4].split(": ")[-1], body[5].split(": ")[-1]

        self.id = int(id)
        self.items = deque(map(int, starting_items.split(", ")))
        self.operation = operation.split(" = ")[-1]
        self.test = int(test.split()[-1])
        self.result = lambda x: int(if_true.split()[-1]) if x else int(if_false.split()[-1])
        self.inspected = 0

    def inspect(self):
        global divisor
        while self.items:
            old = self.items.popleft()
            new = eval(self.operation)
            self.inspected += 1
            # worry_level = new // 3
            worry_level = new % divisor
            yield self.result(worry_level % self.test == 0), worry_level

    def __repr__(self):
        return(
            f"{self.id=}\n"
            f"{self.items=}\n"
            f"{self.operation=}\n"
            f"{self.test=}\n"
            f"{self.result=}\n"
            f"{self.inspected=}\n"
        )


with open(f_in, 'r') as f:
    monkeys = list(map(lambda x: Monkey(x.split("\n")), f.read().split("\n\n")))

for monkey in monkeys:
    divisor *= monkey.test

# for round in range(1, (rounds := 20) + 1):
for round in range(1, (rounds := 10_000) + 1):
    for monkey in monkeys:
        for i, item in monkey.inspect():
            monkeys[i].items.append(item)

monkeys.sort(key=lambda x: x.inspected, reverse=True)

print(monkeys[0].inspected * monkeys[1].inspected)
