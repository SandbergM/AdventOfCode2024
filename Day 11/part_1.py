from data import puzzle_data, example_data
import datetime


data = puzzle_data()

start = datetime.datetime.now()

def func(n, iterations):

    counts = {n : 1}

    for _ in range(iterations):

        cur_counts = {}

        for num, count in counts.items():

            num_str = str(num)

            if num == 0:
                cur_counts[1] = cur_counts.get(1, 0) + count
                
            elif len(num_str) % 2 == 0:
                l = num_str[:len(num_str) // 2]
                r = num_str[len(num_str) // 2:]
                cur_counts[int(l)] = cur_counts.get(int(l), 0) + count
                cur_counts[int(r)] = cur_counts.get(int(r), 0) + count
                
            else:
                cur_counts[num * 2024] = cur_counts.get(num * 2024, 0) + count 

        counts = cur_counts

    return sum(counts.values())

ans = 0

for n in data:
    ans += func(n, 25)

end = datetime.datetime.now()

print("Ans : ", ans) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")