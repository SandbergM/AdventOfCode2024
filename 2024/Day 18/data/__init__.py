
def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")

def __data(file_name):
    with open(f"data/{file_name}.txt", 'r') as f:
        return [tuple(map(int, line.split(",")))[::-1] for line in f.read().splitlines()]