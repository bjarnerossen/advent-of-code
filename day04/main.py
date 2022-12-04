# Part1
with open("input.txt") as file:
    data = file.read()
    data = data.split("\n")

counter1 = 0

for line in data:
    elf1, elf2 = line.split(",")
    x0, y0 = map(int, elf1.split("-"))
    x1, y1 = map(int, elf2.split("-"))

    if x0 >= x1 and y0 <= y1:
        counter1 += 1
    elif x1 >= x0 and y1 <= y0:
        counter1 += 1

# Part2
with open("input.txt") as file:
    data = file.read()
    data = data.split("\n")

counter2 = 0

for line in data:
    elf1, elf2 = line.split(",")
    x0, y0 = map(int, elf1.split("-"))
    x1, y1 = map(int, elf2.split("-"))

    if max(x0, x1) <= min(y0, y1):
        counter2 += 1
        
print("Part1 Answer:",counter1)
print("Part2 Answer:",counter2)

