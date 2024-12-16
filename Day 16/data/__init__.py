
def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")

def __data(file_name):
    with open(f"data/{file_name}.txt", 'r') as f:
        return [list(map(str, line)) for line in f.read().splitlines()]