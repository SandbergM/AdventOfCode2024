from data import puzzle_data, example_data
import datetime
import heapq

data = puzzle_data()

start = datetime.datetime.now()

directions = {(-1, 0): "north", (1, 0): "south", (0, 1): "east", (0, -1): "west"}

def inbounds(x, y, d):
    return 0 <= x < len(d) and 0 <= y < len(d[0]) and d[x][y] != "#"

# Dijkstra's algorithm implementation
def dijkstra(graph, start):

    priority_queue = []
    heapq.heappush(priority_queue, (0, start, ""))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node, direction = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            xa, yy = neighbor
            xb, yb = current_node
            neighbor_direction = directions.get((xa - xb, yy - yb), "")
            distance = current_distance + (1000 if direction and direction != neighbor_direction else 0) + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor, neighbor_direction))
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes

# Graph construction
graph = {}
rotations = {"north": (-1, 0), "south": (1, 0), "east": (0, 1), "west": (0, -1)}
for idx in range(len(data)):
    for jdx in range(len(data[0])):
        if inbounds(idx, jdx, data):
            graph[(idx, jdx)] = {}
            for direction, (dx, dy) in rotations.items():
                if inbounds(idx + dx, jdx + dy, data):
                    graph[(idx, jdx)][(idx + dx, jdx + dy)] = 1  # Edge weight

# Find the start ('S') and end ('E') nodes
start_node = None
end_node = None
for idx, line in enumerate(data):
    if "S" in line:
        start_idx = idx
        start_jdx = line.index("S")
        start_node = (start_idx, start_jdx)
    if "E" in line:
        end_idx = idx
        end_jdx = line.index("E")
        end_node = (end_idx, end_jdx)

# Run Dijkstra's algorithm
if start_node and end_node:
    distances, previous_nodes = dijkstra(graph, start_node)

    # Reconstruct the shortest path
    def reconstruct_path(previous_nodes, start, end):
        path = []
        current = end
        while current:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()
        return path if path[0] == start else []

    shortest_path = reconstruct_path(previous_nodes, start_node, end_node)

    # Output the results
    print("Shortest distances from start node to end node:", distances[end_node])
    # print("Shortest path:", shortest_path)
else:
    print("Start or end node not found!")

# End the timer
end = datetime.datetime.now()
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")
