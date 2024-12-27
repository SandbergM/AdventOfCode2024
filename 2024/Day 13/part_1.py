from data import puzzle_data, example_data
import datetime


data = example_data()

start = datetime.datetime.now()

ans = 0
for el in data:
    print(el)

end = datetime.datetime.now()

print("Ans : ", ans) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")