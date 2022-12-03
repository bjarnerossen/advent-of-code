# Part1
with open("input.txt") as file:
    data = file.read()
    data = data.split("\n")

counter = 0
    
for line in data:
    length = int(len(line) / 2)

    c1 = line[:length]
    c2 = line[length:]

    a = set(c1).intersection(set(c2))

    for char in a:
        if (char.islower()):
            counter += int(ord(f"{char}")-96)
        elif (char.isupper()):
            counter += int(ord(f"{char}")-38)
    
# Part2
with open("input.txt") as file:
    data = file.read()
    data = data.split("\n")

# counter = 0
    
# for line in data:
#     length = int(len(line) / 2)

#     c1 = line[:length]
#     c2 = line[length:]

#     a = set(c1).intersection(set(c2))

#     for char in a:
#         if (char.islower()):
#             counter += int(ord(f"{char}")-96)
#         elif (char.isupper()):
#             counter += int(ord(f"{char}")-38)

print(f"Part1 Answer:",counter)
print(f"Part2 Answer:",counter)
    