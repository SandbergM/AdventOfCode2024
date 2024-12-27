from data import puzzle_data, example_data
import datetime
import heapq

data = puzzle_data()
ans = 0
start = datetime.datetime.now()


slopes = [
    (1,1),
    (1,3),
    (1,5),
    (1,7),
    (2,1),
]

for i, j in slopes:

    jdx = 0
    _ans = 0
    
    for idx in range(i, len(data), i):
        jdx += j
        if data[idx][jdx%len(data[idx])] == "#":
            _ans += 1
    
    ans = ans * _ans if ans else _ans        


print("Ans:", ans)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
