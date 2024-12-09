from data import puzzle_data, example_data
import datetime


data = puzzle_data()

start = datetime.datetime.now()
visual = []
ans = 0

has_more = True
idx = 0

while has_more:

    if len(data):
        free_space = data.pop(0)
        visual.extend([str(idx) for x in range(free_space)])
        idx += 1
    
    if len(data):
        file_block = data.pop(0)
        visual.extend(["." for x in range(file_block)])

    if len(data) == 0:
        has_more = False
ans = 0
x = ""
idx = 0

for idx, el in enumerate(visual):
    print(f"{idx} : {len(visual)}")
    if el == '.':
        for j in range(len(visual) - 1, idx, -1):
            if visual[j] != '.':
                visual[idx], visual[j] = visual[j], visual[idx]
                break

end = datetime.datetime.now()

print(x)
print("Ans : ", sum([ idx * int(el) for idx, el in enumerate(visual) if el != '.'])) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")