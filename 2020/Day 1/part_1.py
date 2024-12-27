from data import puzzle_data, example_data
import datetime
import heapq

data = example_data()
data = {int(x) for x in data}
start = datetime.datetime.now()
ans = 0 

for n in data:
    if 2020 - n in data:
        ans = n  * (2020 - n)
        break

print("Ans:", ans)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
