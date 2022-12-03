from string import ascii_lowercase, ascii_uppercase

# Part1
with open("input.txt") as file:
    data = file.read()
    data = data.split("\n")

counter1 = 0
    
for line in data:
    length = int(len(line) / 2)

    c1 = line[:length]
    c2 = line[length:]

    a = set(c1).intersection(set(c2))

    for char in a:
        if (char.islower()):
            counter1 += int(ord(f"{char}")-96)
        elif (char.isupper()):
            counter1 += int(ord(f"{char}")-38)
    
# Part2
with open("input.txt") as file:
    data = file.read()
    data = data.split("\n")

    counter2 = 0 

    for i in range(0, len(data), 3):
        set1 = set(data[i])
        set2 = set(data[i+1])
        set3 = set(data[i+2])

        shared = set1.intersection(set2, set3)
         
        for char in shared:
            if (char.islower()):
                counter2 += int(ord(f"{char}")-96)
            elif (char.isupper()):
                counter2 += int(ord(f"{char}")-38)

print(f"Part1 Answer:",counter1)
print(f"Part2 Answer:",counter2)
    