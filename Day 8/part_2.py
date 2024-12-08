from data import (
    puzzle_data,
    example_data
)

import datetime
from itertools import combinations

data = puzzle_data()

antennas = "".join(["".join(i) for i in data])
antennas = set([x for x in antennas if x != "."])
indexes = {}

x_max = len(data) + 1
x_min = -1
y_max = len(data[0]) + 1
y_min = -1
d_copy = puzzle_data()
antinode_cords = set()
start = datetime.datetime.now()


antenna_cords = {}

for idx in range(len(data)):
    for jdx in range(len(data[idx])):
        if data[idx][jdx] != ".":
            if antenna_cords.get(data[idx][jdx]) is None:
                antenna_cords[data[idx][jdx]] = []
            antenna_cords[data[idx][jdx]].append((idx, jdx))


for k, v in antenna_cords.items():

    for a, b in combinations(v, r=2):
        
        for idx in range(len(data)):

                a_x, a_y = a
                b_x, b_y = b

                for x, y in [
                    (
                        a_x - (b_x - a_x) * idx,
                        a_y - (b_y - a_y) * idx
                    ),
                    (
                        b_x + (b_x - a_x) * idx,
                        b_y + (b_y - a_y) * idx
                    )
                ]:

                    if 0 <= x < len(data[0]) and  0 <= y < len(data[0]):
                        antinode_cords.add((x, y))

end = datetime.datetime.now()


print("Ans : ", len(antinode_cords))
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")