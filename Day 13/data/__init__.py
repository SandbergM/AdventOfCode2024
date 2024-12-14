import re

def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")


def __data(file_name):
    data = []
    with open(f"data/{file_name}.txt", "r") as file:
        content = file.read().strip()
        entries = content.split("\n\n")
        for entry in entries:
            print(entry)
            lines = entry.split("\n")
            result = {}
            for line in lines:
                if line.startswith("Button A"):
                    result['a'] = tuple(map(int, re.findall(r'\d+', line)))
                elif line.startswith("Button B"):
                    result['b'] = tuple(map(int, re.findall(r'\d+', line)))
                elif line.startswith("Prize"):
                    result['prize'] = tuple(map(int, re.findall(r'\d+', line)))
            data.append(result)
    return data