from data import puzzle_data, example_data
import datetime
import heapq

data = puzzle_data()
ans = 0
start = datetime.datetime.now()

for _min,_max,char,password in data:
    if _min <= password.count(char) <= _max:
        ans += 1

print("Ans:", ans)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
