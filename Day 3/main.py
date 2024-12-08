def read_data(file_name):
    with open(f"{file_name}.txt", 'r') as file:
        return file.read()


import re

def part_1(data) -> int:
    
    regex = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", data)
    ans = 0
    g = True

    for r in regex:
        if r == "do()":
            g = True
        elif r == "don't()":
            g = False

        if g and r != "do()":
            a, b = r[4:-1].split(',')
            ans += int(a) * int(b)

    return ans

print("Example 1 : ", part_1(read_data('example')))
print("Part 1 : ", part_1(read_data('data')))

print("Example 1 : ", part_1(read_data('example')))
print("Part 1 : ", part_1(read_data('data')))