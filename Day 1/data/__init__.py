
def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")

def __data( file_name ):

    left_values = []
    right_values = []

    with open(f"data/{file_name}.txt", 'r') as f:
        for line in f.read().splitlines():
            left, right = map(int, line.split())
            left_values.append(left)
            right_values.append(right)

    return left_values, right_values
