from data import puzzle_data, example_data
import datetime

data = puzzle_data()

start = datetime.datetime.now()

def inbounds(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])

def same_region(a, b):
    x, y = a
    i, j = b
    if not inbounds(x, y) or not inbounds(i, j):
        return False
    return data[x][y] == data[i][j]

def get_neighbour(idx, jdx, char, rotation):
    rotations = {
        "r": (0, 1),
        "d": (1, 0),
        "l": (0, -1),
        "u": (-1, 0),
    }
    nx, ny = idx + rotations[rotation][0], jdx + rotations[rotation][1]
    if inbounds(nx, ny) and data[nx][ny] == char:
        return (nx, ny)
    return None

mappings = {}
for idx in range(len(data)):
    for jdx in range(len(data[idx])):
        char = data[idx][jdx]
        mappings[(idx, jdx)] = {
            "u": get_neighbour(idx, jdx, char, "u"),
            "d": get_neighbour(idx, jdx, char, "d"),
            "l": get_neighbour(idx, jdx, char, "l"),
            "r": get_neighbour(idx, jdx, char, "r"),
        }

seen = set()
ans = 0

for k, v in mappings.items():
    if k in seen:
        continue

    coordinates = [k]
    sides = 0
    areas = 0

    while coordinates:
        current = coordinates.pop()
        if current in seen:
            continue

        x, y = current
        char = data[x][y]
        neighbours = [n for n in mappings[current].values() if n is not None]

        sides += sum([
            int(not same_region((x-1, y), current) and not same_region((x, y+1), current)),
            int(not same_region((x, y+1), current) and not same_region((x+1, y), current)),
            int(not same_region((x+1, y), current) and not same_region((x, y-1), current)),
            int(not same_region((x, y-1), current) and not same_region((x-1, y), current)),
            int(same_region((x-1, y), current) and same_region((x, y+1), current) and not same_region((x-1, y+1), current)),
            int(same_region((x, y+1), current) and same_region((x+1, y), current) and not same_region((x+1, y+1), current)),
            int(same_region((x+1, y), current) and same_region((x, y-1), current) and not same_region((x+1, y-1), current)),
            int(same_region((x, y-1), current) and same_region((x-1, y), current) and not same_region((x-1, y-1), current)),
        ])

        areas += 1
        coordinates.extend([n for n in neighbours if n not in seen])
        seen.add(current)

    ans += sides * areas

end = datetime.datetime.now()

print("Ans:", ans)
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")
