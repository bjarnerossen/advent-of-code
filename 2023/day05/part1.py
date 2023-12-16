import re

def parse_data(data):
    seeds = [int(seed) for seed in re.findall(r'\d+', data[0])]
    
    maps = []
    for line in data[2:]:
        if line.endswith(":"):
            maps.append(dict())
        elif line:
            destination, source, length = [int(number) for number in line.split()]
            maps[-1][range(source, source + length)] = range(destination, destination + length)
    
    return seeds, maps

def find_destination(current_map, value):
    for source_range, destination_range in current_map.items():
        if value in source_range:
            return destination_range.start + (value - source_range.start)
    return value

def lookup_location(initial_value: int, maps: list) -> int:
    value = initial_value
    for current_map in maps:
        value = find_destination(current_map, value)
    return value

def main():
    input_file = "input.txt"
    with open(input_file) as file:
        data = file.read().splitlines()

    seeds, maps = parse_data(data)
    locations = [lookup_location(seed, maps) for seed in seeds]
    print(min(locations))

if __name__ == "__main__":
    main()
