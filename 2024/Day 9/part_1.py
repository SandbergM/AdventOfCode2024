from data import puzzle_data, example_data
import datetime


data = puzzle_data()

start = datetime.datetime.now()

res = []
jdx = 0

for idx, el in enumerate(data):
    
    if idx % 2 == 0:
        for _ in range(el):
            res.append(jdx)
        jdx += 1

    if idx % 2 != 0:
        for _ in range(el):
            res.append(None)

idx = 0
ans = 0

while True:

    if len(res) == 0:
        break

    e = res.pop(0)

    if e is None:

        while True:
            
            if len(res) == 0:
                break
            
            e = res.pop()
            
            if e is not None:
                ans += (idx * e)
                break

    else:
        ans += (idx * e)

    idx += 1

end = datetime.datetime.now()

print("Ans : ", ans) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")