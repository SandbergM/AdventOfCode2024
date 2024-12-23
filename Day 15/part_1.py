from data import puzzle_data, example_data
import datetime


grid, moves = puzzle_data()

start = datetime.datetime.now()

movable_tiles = {}
current = None

for idx in range(len(grid)):
    for jdx in range(len(grid[idx])):
        
        char = grid[idx][jdx]

        if char == "@":
            current = (idx, jdx)
            grid[idx][jdx] = "."
            char = "."
        
        if grid[idx][jdx] not in ["#"]:
            movable_tiles[(idx, jdx)] = char

directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

for move in moves:

    cords, tiles = [], []
    dx, dy = directions[move]
    x,y = current

    while True:

        x, y = x + dx, y + dy

        if (x, y) not in movable_tiles:
            break

        tiles.append(movable_tiles[(x, y)])
        cords.append((x, y))

        if movable_tiles[(x, y)] == ".":
            current = (current[0] + dx, current[1] + dy)
            break

    for tile, cord in zip(tiles, cords[::-1]):
        movable_tiles[cord] = tile

ans = 0

for k, v in movable_tiles.items():
    if v == "O":
        ans += 100 * (k[0]) + (k[1])

end = datetime.datetime.now()

print("Ans : ", ans) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")