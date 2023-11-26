# Part1
with open("input.txt") as file:
    data = ""
    data += file.read().strip().lower()

marker = []
counter = 0

for char in data:
    marker.append(char) 
    counter += 1
    if len(marker) == 4:
        if len(set(marker)) != 4:
            marker.pop(0)
            continue
        else:
            print(marker)
            print(f"Part1 Answer: {counter}")
            pass
    else: 
        continue



# Part2
marker = []
counter = 0

for char in data:
    marker.append(char) 
    counter += 1
    if len(marker) == 14:
        if len(set(marker)) != 14:
            marker.pop(0)
            continue
        else:
            print(marker)
            print(f"Part2 Answer: {counter}")
            pass
    else: 
        continue