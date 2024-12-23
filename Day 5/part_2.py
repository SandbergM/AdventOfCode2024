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

rules = set(rules)

ans = 0


def is_good_update(update, mappings):

    previous = []
    update_copy = update.copy()

    while update_copy:

        curr_element = update_copy.pop(0)
        mapping = mappings[curr_element]

        if any([pre not in mapping["pre"] for pre in previous]):
            return False

        if any([post not in mapping["post"] for post in update_copy]):
            return False

        previous.append(curr_element)

    return True

for update in updates:

    if is_good_update(update, mappings):
        continue

    while True:

        for idx in range(len(update) - 1):
            if (update[idx], update[idx+1]) not in rules:
                update[idx], update[idx+1] = update[idx+1], update[idx]

        if is_good_update(update, mappings):
            break

    ans += update[len(update)  // 2]

end = datetime.datetime.now()

print("Ans:", ans)
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")
