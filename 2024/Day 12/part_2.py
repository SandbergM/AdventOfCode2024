from data import puzzle_data, example_data
import datetime

data = puzzle_data()

start = datetime.datetime.now()

def get_neighbour(idx, jdx, char, rotation):

    r_x, y_x = {
        "r": (0, 1),
        "d": (1, 0),
        "l": (0, -1),
        "u": (-1, 0),
    }.get(rotations)

    nx, ny = idx + r_x, jdx + y_x

    if inbounds(nx, ny) and data[nx][ny] == char:
        return (nx, ny)

    return None

mappings = {}
chars = {}
for idx in range(len(data)):
    for jdx in range(len(data[idx])):
        char = data[idx][jdx]
        chars[(idx, jdx)] = char
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

        # convex corners
        sides += int(chars.get((x-1, y)) != char and chars.get((x, y+1)) != char)
        sides += int(chars.get((x, y+1)) != char and chars.get((x+1, y)) != char)
        sides += int(chars.get((x+1, y)) != char and chars.get((x, y-1)) != char)
        sides += int(chars.get((x, y-1)) != char and chars.get((x-1, y)) != char)

        #concave corners
        sides += int(chars.get((x-1, y)) == char and chars.get((x, y+1)) == char and chars.get((x-1, y+1)) != char)
        sides += int(chars.get((x, y+1)) == char and chars.get((x+1, y)) == char and chars.get((x+1, y+1)) != char)
        sides += int(chars.get((x+1, y)) == char and chars.get((x, y-1)) == char and chars.get((x+1, y-1)) != char)
        sides += int(chars.get((x, y-1)) == char and chars.get((x-1, y)) == char and chars.get((x-1, y-1)) != char)

        areas += 1
        coordinates.extend([n for n in neighbours if n not in seen])
        seen.add(current)

    ans += sides * areas

end = datetime.datetime.now()

print("Ans:", ans)
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")
