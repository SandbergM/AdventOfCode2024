from itertools import combinations
from data import puzzle_data
import datetime


data = puzzle_data()

antennas = "".join(["".join(i) for i in data])
antennas = set([x for x in antennas if x != "."])
indexes = {}

x_max = len(data)
y_max = len(data[0])
antinode_cords = set()

start = datetime.datetime.now()

antenna_cords = {}

for idx in range(x_max):
    for jdx in range(y_max):
        if data[idx][jdx] != ".":

            if antenna_cords.get(data[idx][jdx]) is None:
                antenna_cords[data[idx][jdx]] = []

            antenna_cords[data[idx][jdx]].append((idx, jdx))


for k, v in antenna_cords.items():

    for a, b in combinations(v, r=2):
            
            a_x, a_y = a
            b_x, b_y = b

            x, y = a_x - (b_x - a_x), a_y - (b_y - a_y)
            z, w = b_x + (b_x - a_x), b_y + (b_y - a_y)

            if 0 <= x < x_max and 0 <= y < x_max:
                antinode_cords.add((x, y))
                
            if 0 <= z < x_max and 0 <= w < x_max:
                antinode_cords.add((z, w))

end = datetime.datetime.now()


print("Ans : ", len(antinode_cords))
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")