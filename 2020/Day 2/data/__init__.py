import re


def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")

def __data(file_name):
    data = []
    with open(f"data/{file_name}.txt", 'r') as f:
        for line in f.read().splitlines():
            match = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
            if match:
                min_count, max_count, char, password = match.groups()
                data.append((int(min_count), int(max_count), char, password))
    
    return data