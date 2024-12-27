# from data import puzzle_data, example_data
# import datetime
# import heapq

# data = puzzle_data()[:1024]
# full_data = set(puzzle_data())
# start = datetime.datetime.now()

# x_len = 71
# y_len = 71

# start_node = (0,0)
# end_node = (70,70)

# grid = [["." for j in range(x_len)] for i in range(y_len)]

# for x,y in data:
#     grid[x][y] = "#"

# graph = {}
# rotations = [(0,1),(1,0),(0,-1),(-1,0)]

# def in_bounds(x,y):
#     return 0 <= x < x_len and 0 <= y < y_len and grid[x][y] != "#"

# for idx in range(len(grid)):
#     for jdx in range(len(grid[idx])):
#         if in_bounds(idx, jdx):
#             graph[(idx, jdx)] = []
#             for dx, dy in rotations:
#                 if in_bounds(idx + dx, jdx + dy):
#                     graph[(idx, jdx)].append((idx + dx, jdx + dy))

# def deijkstra(graph, start, end):

#     priority_queue = [(0, start)]
#     distances = {node: float('infinity') for node in graph}
#     distances[start] = 0
#     previous_nodes = {node: None for node in graph}

#     while priority_queue:

#         current_distance, current_node = heapq.heappop(priority_queue)
#         if current_distance > distances[current_node]:
#             continue

#         for neighbor in graph[current_node]:

#             distance = current_distance + 1
            
#             nx, ny = neighbor

#             if distance < distances[neighbor] and in_bounds(nx,ny):
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, (nx, ny)))
#                 previous_nodes[neighbor] = current_node

#     return distances, previous_nodes

# def assemble_shortest_path(start, end, previous_nodes):

#     path = []

#     while end:
#         path.append(end)
#         end = previous_nodes[end]

#     return path

# d, p = deijkstra(graph, start_node, end_node)

# cords = assemble_shortest_path(start_node, end_node, p)

# for cord in full_data:
#     if cord in cords:
#         print(cord[::-1])
#         break

# print("Ans:", len(cords) - 1)  
# print(f"Time taken: {(datetime.datetime.now() - start).total_seconds() * 1000:.2f} ms")






haystack = "abc"
needle = "c"
def strStr(haystack: str, needle: str) -> int:

    if haystack == needle:
        return 0

    needle_len = len(needle)

    if needle_len == 1:
        for idx in range(len(haystack)):
            if haystack[idx] == needle:
                return idx
        return -1

    for idx in range(needle_len, len(haystack) + 1):
        if haystack[idx - needle_len: idx] == needle:
            return idx - needle_len

    return -1

print(strStr(haystack, needle))



def search(self, nums: List[int], target: int) -> int:

    idx = len(nums) // 2

    while True:

        if 0 <= idx < len(nums):
            return -1

        n = nums[idx]
        
        if n == target:
            return idx

        if n > 
    
    return -1