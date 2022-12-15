from pathlib import Path
from collections import deque

path = Path(__file__)

f_in = f"{path.parent}/.in"



class HeightMap():
    class Node():
        def __init__(self, coordinate, value):
            self.coordinate = coordinate
            self.value = value
            self.connections = []

        def add_connection(self, node):
            self.connections.append(node)

        def __repr__(self):
            return f"{self.coordinate}[{self.value}]->{list(_.coordinate for _ in self.connections)}"

    def __init__(self, lines):
        heights = []
        for j, line in enumerate(lines):
            heights.append([])
            for i, char in enumerate(line.strip()):
                if char.islower():
                    heights[j].append(HeightMap.Node((i, j), ord(char) - 97))
                elif char == "S":
                    start_node = HeightMap.Node((i, j), 0)
                    self.start = start_node
                    heights[j].append(start_node)
                elif char == "E":
                    end_node = HeightMap.Node((i, j), 25)
                    self.end = end_node
                    heights[j].append(end_node)
        self.graph = self.create_graph(heights)

    def create_graph(self, heights):
        for j, _ in enumerate(heights):
            for i, node in enumerate(_):
                if node.coordinate == self.end.coordinate:
                    # don't allow connections from end
                    break
                if i - 1 >= 0:
                    if heights[j][i - 1].value <= node.value + 1:
                        node.add_connection(heights[j][i - 1])
                if i + 1 <= len(_) - 1:
                    if heights[j][i + 1].value <= node.value + 1:
                        node.add_connection(heights[j][i + 1])
                if j - 1 >= 0:
                    if heights[j - 1][i].value <= node.value + 1:
                        node.add_connection(heights[j - 1][i])
                if j + 1 <= len(heights) - 1:
                    if heights[j + 1][i].value <= node.value + 1:
                        node.add_connection(heights[j + 1][i])

    def bfs(self):
        visited = set()
        queue = deque([self.start])
        while queue:
            current = queue.popleft()
            print(current.coordinate)
            if current.coordinate == self.end.coordinate:
                return visited
            for neighbour in current.connections:
                if neighbour.coordinate not in visited:
                    visited.add(neighbour.coordinate)
                    queue.append(neighbour)

with open(f_in, 'r') as f:
    height_map = HeightMap(f.readlines())

# print("\n".join(["".join(f"{_:2}" for _ in col) for col in height_map.heights]))
print(height_map.start, height_map.end)

print(height_map.bfs())
