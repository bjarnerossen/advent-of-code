# Part1
with open("input.txt") as file:
    data = file.read()
    data = data.split("\n")

counter1 = 0
counter2 = 0

for line in data:
    elf1, elf2 = line.split(",")
    a, b = map(int, elf1.split("-"))
    c, d = map(int, elf2.split("-"))

    if a >= c and b <= d:
        counter1 += 1
    elif c >= a and d <= b:
        counter1 += 1

# Part2
    if max(a, c) <= min(b, d):
        counter2 += 1
        
print("Part1 Answer:",counter1)
print("Part2 Answer:",counter2)

