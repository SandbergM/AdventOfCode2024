from data import puzzle_data, example_data
import datetime
import heapq

data = puzzle_data()
ans = 0
start = datetime.datetime.now()

def is_valid_year(val, min, max):
    
    if val is None:
        return False

    return min <= int(val) <= max

def is_valid_height(h_val):
    
    if h_val is None:
        return False
    
    if h_val.endswith("cm"):
        return 150 <= int(h_val[:-2]) <= 193
    elif h_val.endswith("in"):
        return 59 <= int(h_val[:-2]) <= 76
    else:
        return False

def is_valid_hair_color(hcl):
    
    if hcl is None:
        return False

    if hcl[0] != "#":
        return False

    return all([c in "0123456789abcdef" for c in hcl[1:]]) and len(hcl) == 7

def is_valid_eye_color(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_valid_pid(pid):

    if pid is None:
        return False

    return len(pid) == 9 and pid.isdigit()

for idx, d in enumerate(data):
    ans += all([
        is_valid_year(d.get("byr"), 1920, 2002),
        is_valid_year(d.get("iyr"), 2010, 2020),
        is_valid_year(d.get("eyr"), 2020, 2030),
        is_valid_height(d.get("hgt")),
        is_valid_hair_color(d.get("hcl")),
        is_valid_eye_color(d.get("ecl")),
        is_valid_pid(d.get("pid")),
    ])

print("Ans:", ans)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
