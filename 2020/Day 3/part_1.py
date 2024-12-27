from data import puzzle_data, example_data
import datetime
import heapq

data = example_data()
ans = 0
start = datetime.datetime.now()

jdx = 0

for idx in range(1, len(data)):

    jdx += 3

    if data[idx][jdx%len(data[idx])] == "#":
        ans += 1

print("Ans:", ans)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
