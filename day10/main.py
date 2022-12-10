# Part1
with open("input.txt") as f:
    signals = f.read().splitlines()

    x = 1
    cycles = (20, 60, 100, 140, 180, 220)
    cycle = part1 = 0 

    for signal in signals:  
        if signal.startswith("noop"):
            cycle += 1
            if cycle in cycles:
                part1 += cycle * x

        else:
            for i in range(2):
                   cycle += 1
                   if cycle in cycles:
                       part1 += cycle * x
                   if i == 1:
                       x += int(signal.split()[1])

print("Part1 Answer:", part1)

# Part2
crt = ""
cycle = 1
x = 1

for signal in signals:
    if (cycle - 1) % 40 == 0:
        crt += "\n"
    crt += "#" if (cycle - 1) % 40 in (x - 1, x, x + 1) else " "

    if signal.startswith("noop"):
        cycle += 1
    else:
        if cycle % 40 == 0:
            crt += "\n"
        crt += "#" if cycle % 40 in (x - 1, x, x + 1) else " "
        cycle += 2
        x += int(signal.split()[1])

print("Part2 Answer:",crt)