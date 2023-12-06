with open("./data/input_12.txt", "r") as f:
    entries = [entry.strip() for entry in f]

nodes = dict()
locations = dict()
start_locations = list()

START_NODE = None
END_NODE = None

for idx_y, entry in enumerate(entries):
    for idx_x, col in enumerate(entry):
        loc = (idx_x, idx_y)

        if col == 'S':
            START_NODE = loc
            col = 'a'
        elif col == 'E':
            END_NODE = loc
            col = 'z'

        locations[loc] = col

        if col == 'a':
            start_locations.append(loc)


for idx_y in range(0, len(entries)):
    for idx_x in range(0, len(entries[0])):
        col = locations[(idx_x, idx_y)]
        loc = (idx_x, idx_y)

        nodes[loc] = set()

        # check north
        if idx_y > 0:
            north_value = locations[(idx_x, idx_y-1)]
            if ord(north_value) - ord(col) <= 1:
                nodes[loc].add((idx_x, idx_y-1))

        # check south
        if idx_y < len(entries) - 1:
            south_value = locations[(idx_x, idx_y+1)]
            if ord(south_value) - ord(col) <= 1:
                nodes[loc].add((idx_x, idx_y+1))

        # check west
        if idx_x > 0:
            west_value = locations[(idx_x-1, idx_y)]
            if ord(west_value) - ord(col) <= 1:
                nodes[loc].add((idx_x-1, idx_y))

        # check east
        if idx_x < len(entries[0]) - 1:
            east_value = locations[(idx_x+1, idx_y)]
            if ord(east_value) - ord(col) <= 1:
                nodes[loc].add((idx_x+1, idx_y))


def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

print(f'Start: {START_NODE}, End: {END_NODE}')

result = shortest_path(nodes, START_NODE, END_NODE)
print(len(result)-1)

min_path = 100000

for location in start_locations:
    result = len(shortest_path(nodes, location, END_NODE))-1

    if result > -1:
        min_path = min(result, min_path)

print(min_path)



# for loc, paths in nodes.items():
#     print(loc, paths)

