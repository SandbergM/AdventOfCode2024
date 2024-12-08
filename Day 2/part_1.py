from collections import Counter
from data import puzzle_data, example_data
import time 

# data = example_data()
data = puzzle_data()

total_time = 0
runs = 1 # 25



for _ in range(runs):

    start_time = time.time()
    
    ### LOGIC STARTS HERE ###
    ans = 0
    for l in data:
        
        l_sorted = sorted(l)
        l_reversed = sorted(l, reverse=True)
        diffs = [abs(l[idx] - l[idx - 1]) for idx in range(1, len(l))]
        contains_no_duplicates = len(l) == len(set(l))
        biggest_diff = max(diffs)

        if l != l_sorted and l != l_reversed or biggest_diff > 3 or not contains_no_duplicates:
            continue

        ans += 1

    ### LOGIC ENDS HERE ###

    end_time = time.time()
    total_time += (end_time - start_time) * 1000

avg_time = total_time / runs

print("Answer : ", ans)
print(f"Average execution time over {runs} runs: {avg_time:.2f} ms")
