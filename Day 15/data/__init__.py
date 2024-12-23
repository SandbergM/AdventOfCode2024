
import re

def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")



def __data(file_name):
    with open(f"./data/{file_name}.txt", 'r') as file:
        lines = file.readlines()
    
    grid_data = []
    directions_data = []
    empty_line_found = False
    
    for line in lines:
        
        stripped_line = line.strip()

        if not stripped_line:
            empty_line_found = True
            continue
        
        if not empty_line_found:
            grid_data.append(list(stripped_line))
        else:
            directions_data.extend(stripped_line)
    
    return grid_data, directions_data