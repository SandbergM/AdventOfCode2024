def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")

def __data( file_name ):

    left_values = []
    right_values = []

    with open(f"data/{file_name}.txt", 'r') as f:
        return [[int(value) for value in line.split(" ")] for line in f.read().splitlines()]
