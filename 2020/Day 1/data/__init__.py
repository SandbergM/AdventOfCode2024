
def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")

def __data(file_name):
    data = []
    with open(f"data/{file_name}.txt", 'r') as f:
        for line in f.read().splitlines():
            data.append(int(line))
    
    return data