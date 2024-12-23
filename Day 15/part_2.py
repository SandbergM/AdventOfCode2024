from data import puzzle_data, example_data
import datetime


__grid, moves = example_data()

start = datetime.datetime.now()

def fatten_grid(grid):

    grid = []

    for idx in range(len(__grid)):
        
        grid.append([])

        for jdx in range(len(__grid[idx])):
            
            char = __grid[idx][jdx]

            if char == "O":
                grid[idx].append("[")
                grid[idx].append("]")

            if char == "#":
                grid[idx].append("#")
                grid[idx].append("#")

            if char == "@":
                grid[idx].append("@")
                grid[idx].append(".")

            if char == ".":
                grid[idx].append(".")
                grid[idx].append(".")
    
    return grid

grid = fatten_grid(__grid)
movable_tiles = {}
current = None

for idx in range(len(grid)):

    for jdx in range(len(grid[idx])):
        
        char = grid[idx][jdx]

        if char == "@":
            current = (idx, jdx)
            grid[idx][jdx] = "."
            char = "."
        
        if grid[idx][jdx] != "#":
            movable_tiles[(idx, jdx)] = char

directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

def horizontal(x, y, direction):

    cords, tiles = [], []
    dx, dy = directions[move]
    initial, next_step = (x,y), (x + dx, y + dy)
    x,y = current

    while True:

        x, y = x + dx, y + dy

        if (x, y) not in movable_tiles:
            break

        tiles.append(movable_tiles[(x, y)])
        cords.append((x, y))

        if movable_tiles[(x, y)] == ".":
            break

    for tile, cord in zip(tiles, cords[::-1]):
        movable_tiles[cord] = tile

    if next_step in movable_tiles and  movable_tiles[next_step] == ".":
        return next_step

    return initial 

def vertical(x, y, direction):

    changes = {}
    dx, dy = directions[direction]
    initial, next_step = (x, y), (x + dx, y + dy)
    to_check = [(x + dx, y + dy)]
    seen = set()
    imposible = False

    while to_check:

        x, y = to_check.pop(0)

        if (x, y) in seen:
            continue

        seen.add((x, y))

        if (x, y) not in movable_tiles:
            imposible = True
            break
        
        char = movable_tiles[(x, y)]

        if char in ["[", "]"]:
            to_check.append((x, y + (-1 if char == "]" else 1)))
        
        if changes.get(x) is None:
            changes[x] = {
                "tiles": [],
                "cords": []
            }

        changes[x]["cords"].append((x, y))
        changes[x]["tiles"].append(char)

    if not imposible:
        for k, v in changes.items():
            for tile, cord in zip(v["tiles"], v["cords"][::-1]):
                movable_tiles[cord] = tile

    if next_step in movable_tiles and  movable_tiles[next_step] == ".":
        return next_step

    return initial

for move in moves:

    __x = fatten_grid(example_data())
    __x[current[0]][current[1]] = "@"

    for line in __x:
        print("".join(line))

    x, y = {
        ">": horizontal, 
        "<": horizontal, 
        "^": vertical, 
        "v": vertical
    }[move](current[0], current[1], move)

    current = (x, y)
ans = 0
end = datetime.datetime.now()

print("Ans : ", sum([ 100 * idx + jdx for idx, jdx in movable_tiles.keys() if movable_tiles[(idx, jdx)] == "["])) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")