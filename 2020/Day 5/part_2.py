from data import puzzle_data, example_data
import datetime

data = puzzle_data()
ans = 0
start = datetime.datetime.now()
seats = set()

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

    seats.add(r[0] * 8 + c[0])

my_seat = -1

for seat in seats:
    if seat + 1 not in seats and seat + 2 in seats:
        my_seat = seat + 1
        break

print("Ans:", my_seat)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
