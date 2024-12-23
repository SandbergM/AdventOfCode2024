
def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")


def __data(file_path):
    with open(f"./data/{file_path}.txt", 'r') as file:
        input_str = file.read()
    
    pairs_str, lists_str = input_str.strip().split('\n\n')
    
    pairs = [tuple(map(int, line.split('|'))) for line in pairs_str.split('\n')]
    lists = [list(map(int, line.split(','))) for line in lists_str.split('\n')]
    
    return pairs, lists