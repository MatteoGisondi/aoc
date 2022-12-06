from pathlib import Path
from collections import Counter

path = Path(__file__)

f_in = f'{path.parent}/.in'

with open(f_in, 'r') as f:
    chars = f.read()

print(chars[:])

def check(chars):
    for i, c in enumerate(chars):
        print(c)
        stream = Counter(chars[i:i+14])
        print(stream)
        if all(map(lambda x: x == 1, stream.values())):
            return i + 14

answer = check(chars)
print(answer)
