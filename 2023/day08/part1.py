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

current_node = "AAA"
steps = 0
instruction = directions()
while current_node != "ZZZ":
    next_left, next_right = network[current_node]
    current_node = next_left if next(instruction) == "L" else next_right
    steps += 1

print(steps)
