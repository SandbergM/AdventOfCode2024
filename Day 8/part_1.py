from data import (
    puzzle_data,
    example_data
)

import datetime


data = puzzle_data()

antennas = "".join(["".join(i) for i in data])
print(set([x for x in antennas if x != "."]))
antennas = set([x for x in antennas if x != "."])

indexes = {}

x_max = len(data) + 1
x_min = -1
y_max = len(data[0]) + 1
y_min = -1

antinode_cords = set()
antinodes = set()
start = datetime.datetime.now()

for idx in range(len(data)):

    for jdx in range(len(data[idx])):

        if data[idx][jdx] in antennas:

            if indexes.get(data[idx][jdx]) is None:
                indexes[data[idx][jdx]] = []

            indexes[data[idx][jdx]].append((idx, jdx))

for a_type, a_cords in indexes.items():

    for idx in range(len(a_cords)):

        for jdx in range(len(a_cords)):

            if idx == jdx:
                continue

            cord_a = a_cords[idx]
            cord_b = a_cords[jdx]

            x_a, y_a = cord_a
            x_b, y_b = cord_b

            x_a_diff = x_a - x_b
            y_a_diff = y_a - y_b

            x_b_diff = x_b - x_a
            y_b_diff = y_b - y_a

            for c in [
                (x_a + x_a_diff, y_a + y_a_diff),
                (x_b + x_b_diff, y_b + y_b_diff),
            ]:
                c_a, c_b = c

                if 0 <= c_a < len(data) and 0 <= c_b < len(data[0]):
                    if data[c_a][c_b] == ".":
                        antinode_cords.add(f"{sorted([ x_a, y_a, x_b, y_b])}|{c_a},{c_b}")


end = datetime.datetime.now()

# for anti in antinode_cords:
#     print(anti)
#     _, cords = anti.split("|")
#     a, b = [int(x) for x in cords.split(",")]
#     data[a][b] = "X"

# for d in data:
#     print("".join(d))

print(len(antinode_cords))
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")