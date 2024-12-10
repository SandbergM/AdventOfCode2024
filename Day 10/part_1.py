from data import puzzle_data, example_data
import datetime


data = puzzle_data()

start = datetime.datetime.now()

starts = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            starts.append((i, j))

def valid_steps(x, y, data, visited):

    next_steps = []
    
    steps = [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1)
    ]

    for step in steps:

        new_x = x + step[0]
        new_y = y + step[1]

        if (new_x, new_y) in visited:
            continue

        if 0 <= new_x < len(data) and 0 <= new_y < len(data[new_x]):
            if data[new_x][new_y] == data[x][y] + 1:
                next_steps.append((new_x, new_y))
    
    return next_steps

ans = 0

for x, y in starts:

    visited = set()
    steps = [(x,y)]

    while steps:

        x, y = steps.pop(0)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if data[x][y] == 9:
            ans += 1
        else:
            steps.extend(valid_steps(x, y, data, visited))


end = datetime.datetime.now()

print("Ans : ", ans) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")