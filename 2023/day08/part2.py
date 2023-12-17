with open("input.txt") as file:
    data = file.read().splitlines()

    network = {}
for line in data[2:]:
    parts = line.split(' = (')
    node = parts[0]
    connections = parts[1].rstrip(')').split(', ')
    left, right = connections
    network[node] = (left, right)

def directions():
    directions = data[0]
    while True:
        for direction in directions:
            yield direction 

counters = []
starting_nodes = [node for node in network.keys() if node.endswith("A")]
for starting_node in starting_nodes:
    current_node = starting_node
    counter = 0
    instruction = directions()
    while not current_node.endswith('Z'):
        next_left, next_right = network[current_node]
        current_node = next_left if next(instruction) == 'L' else next_right
        counter += 1
    counters.append(counter)


print(counters)