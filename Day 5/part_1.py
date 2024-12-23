from data import puzzle_data, example_data
import datetime
import heapq

rules, updates = puzzle_data()

start = datetime.datetime.now()

mappings = {}

for rule in rules:
    a, b = rule

    if a not in mappings:
        mappings[a] = {
            "pre" : set(),
            "post" : set()
        }

    if b not in mappings:
        mappings[b] = {
            "pre" : set(),
            "post" : set()
        }

    mappings[a]["post"].add(b)
    mappings[b]["pre"].add(a)

ans = 0

for update in updates:

    update = list(update)
    previous = []
    good_update = True

    while update:

        curr_element = update.pop(0)
        mapping = mappings[curr_element]
        
        if any([pre not in mapping["pre"] for pre in previous]):
            good_update = False
            break

        if any([post not in mapping["post"] for post in update]):
            good_update = False
            break

        previous.append(curr_element)
        
    if good_update:
        ans += previous[len(previous)  // 2]

end = datetime.datetime.now()
print("Ans:", ans)
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")
