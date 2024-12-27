import re

def puzzle_data():
    return __data("data")

def example_data():
    return __data("example")


def __data(file_name):
    
    data = []

    with open(f"data/{file_name}.txt", "r") as file:
        lines = file.readlines()
        
        for idx in range(0, len(lines), 4):
            data.append({
                "Button A": {
                    "x": int(lines[idx].split("X+")[1].split(",")[0]),
                    "y": int(lines[idx].split("Y+")[1]),
                },
                "Button B": {
                    "x": int(lines[idx+1].split("X+")[1].split(",")[0]),
                    "y": int(lines[idx+1].split("Y+")[1]),
                },
                "Prize": {
                    "x": int(lines[idx+2].split("X=")[1].split(",")[0]),
                    "y": int(lines[idx+2].split("Y=")[1]),
                }
            })

    return data
