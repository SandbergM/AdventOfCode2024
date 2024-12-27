from data import puzzle_data, example_data
import datetime


data = example_data()

start = datetime.datetime.now()


def get_neighbour(idx, jdx, char, rotation):

    rotations = {
        "r" : (0, 1),
        "d" : (1, 0),
        "l" : (0, -1),
        "u" : (-1, 0),
    }

    nx, ny = idx + rotations[rotation][0], jdx + rotations[rotation][1]

    conditions = [
        nx < 0,
        nx >= len(data),
        ny < 0,
        ny >= len(data[0]),
    ]

    if any(conditions):
        return None

    if char == data[nx][ny]:
        return (nx, ny)

    return None

mappings = {}

for idx in range(len(data)):
    for jdx in range(len(data[idx])):
        char = data[idx][jdx]
        mappings[(idx,jdx)] = {
            "u" : get_neighbour(idx, jdx, char, "u"),
            "d" : get_neighbour(idx, jdx, char, "d"),
            "l" : get_neighbour(idx, jdx, char, "l"),
            "r" : get_neighbour(idx, jdx, char, "r"),
        }

seen = set()
ans = 0

for k, v in mappings.items():

    coordinates = [k, *[v for v in mappings[k].values() if v is not None]]
    fences = 0
    areas = 0

    if k in seen:
        continue

    while True:

        if len(coordinates) == 0:
            break

        current = coordinates.pop(0)

        if current in seen:
            continue
        
        neighbours = [v for v in mappings[current].values() if v is not None]
        fences += 4 - len(neighbours)
        areas += 1
        coordinates.extend([n for n in neighbours if n not in seen])
        seen.add(current)

    ans += fences * areas 

end = datetime.datetime.now()

print("Ans : ", ans) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")