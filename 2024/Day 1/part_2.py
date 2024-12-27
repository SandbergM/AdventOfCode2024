
from collections import Counter
from data import puzzle_data
import time

data = puzzle_data()

runs = 25

total_time = 0
result = None

for _ in range(runs):

    start_time = time.time()

    a, b = data
    a.sort()
    b.sort()
    ans = 0

    counts_b = Counter(b)

    for x,y in zip(a,b):
        ans += x * counts_b[x]

    end_time = time.time()
    total_time += (end_time - start_time) * 1000

avg_time = total_time / 25

print("Answer : ", ans)
print(f"Average execution time over {runs} runs: {avg_time:.2f} ms")