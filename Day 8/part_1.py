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

max_x = len(data)

antenna_cords = {}

for idx in range(len(data)):
    for jdx in range(len(data[idx])):
        if data[idx][jdx] != ".":
            if antenna_cords.get(data[idx][jdx]) is None:
                antenna_cords[data[idx][jdx]] = []
            antenna_cords[data[idx][jdx]].append((idx, jdx))


for k, v in antenna_cords.items():

    for a, b in combinations(v, r=2):
        
        a_x, a_y = a
        b_x, b_y = b

        for x, y in [
            (
                a_x - (b_x - a_x),
                a_y - (b_y - a_y)
            ),
            (
                b_x + (b_x - a_x),
                b_y + (b_y - a_y)
            )
        ]:

            if 0 <= x <  and max_x 0 <= y < max_x:
                antinode_cords.add((x, y))
            else:
                break

end = datetime.datetime.now()


print("Ans : ", len(antinode_cords))
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")