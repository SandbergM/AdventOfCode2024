import re


def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")

def __data(file_name):
    
    data = []

    with open(f"data/{file_name}.txt", 'r') as f:

        idx = 0
        curr = ""

        for line in f.read().splitlines():
            if line != "":
                curr = curr + " " + line
            else:
                data.append(curr.strip())
                curr = ""

        data.append(curr.strip())
        
    for row in data:
        data[data.index(row)] = dict(map(lambda x: x.split(":"), row.split(" " )))

    return data
