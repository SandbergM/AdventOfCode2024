from data import puzzle_data, example_data
import datetime
import math

data = puzzle_data()
ans = 0
start = datetime.datetime.now()
highest_boarding_pass = 0

for boarding_pass in data:

    r, c = (0,127), (0, 7)
    rd, cd = 0, 0
    for action in list(boarding_pass):
        
        rdiff = r[1] - r[0]
        cdiff = c[1] - c[0]

        if action == "F":
            r = (r[0], r[0] + (rdiff // 2))
            rd = 0
        elif action == "B":
            r = (r[1] - (rdiff // 2), r[1])
            rd = 1
        elif action == "L":
            c = (c[0], c[0] + (cdiff // 2))
            cd = 0
        elif action == "R":
            c = (c[1] - (cdiff // 2), c[1])
            cd = 1

    highest_boarding_pass = max(highest_boarding_pass, r[0] * 8 + c[0])

print("Ans:", highest_boarding_pass)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
