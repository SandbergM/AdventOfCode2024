from data import puzzle_data, example_data
import datetime
import heapq

data = puzzle_data()
nums = {int(x) for x in data}
start = datetime.datetime.now()
ans = 0 

for idx in range(len(data)):
    for jdx in range(idx + 1, len(data)):
        if 2020 - data[idx] - data[jdx] in data:
            ans = data[idx] * data[jdx] * (2020 - data[idx] - data[jdx])
            break

    if ans:
        break

print("Ans:", ans)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
