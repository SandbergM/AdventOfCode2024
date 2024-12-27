from data import puzzle_data, example_data
import datetime
import heapq

data = puzzle_data()
ans = 0
start = datetime.datetime.now()

required_fields = {
    "byr", # (Birth Year)
    "iyr", # (Issue Year)
    "eyr", # (Expiration Year)
    "hgt", # (Height)
    "hcl", # (Hair Color)
    "ecl", # (Eye Color)
    "pid", # (Passport ID)
}

optional_fields = {
    "cid", # (Country ID)
}

for idx, d in enumerate(data):

    missing_fields = False

    for rf in required_fields:
        if rf not in d.keys():
            missing_fields = True
            break

    ans += int(not missing_fields)

print("Ans:", ans)
print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")
