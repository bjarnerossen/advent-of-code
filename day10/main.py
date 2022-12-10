# Part1
with open("input.txt") as f:
    signals = f.read().splitlines()

    x = 1
    cycles = {"20": 0, "60": 0, "100": 0, "140": 0, "180": 0, "220": 0}
    cycle = 0 

    for signal in signals:
        if signal != "noop":
            for i in range(2):
                cycle += 1
                match cycle:
                     case 20:
                         cycles["20"] += (x * 20)
                     case 60:
                         cycles["60"] += (x * 60)
                     case 100:
                         cycles["100"] += (x * 100)
                     case 140:
                         cycles["140"] += (x * 140)
                     case 180:
                         cycles["180"] += (x * 180)
                     case 220:
                         cycles["220"] += (x * 220)
                if i == 1:
                    _, val = signal.split()
                    x += int(val)

            
        if signal.startswith("noop"):
            cycle += 1
            match cycle:
                   case 20:
                       cycles["20"] += (x * 20)
                   case 60:
                       cycles["60"] += (x * 60)
                   case 100:
                       cycles["100"] += (x * 100)
                   case 140:
                       cycles["140"] += (x * 140)
                   case 180:
                       cycles["180"] += (x * 180)
                   case 220:
                       cycles["220"] += (x * 220)

print("Part1 Answer:", sum(value for value in cycles.values()))

# Part2
crt = ""
cycle = 1
value = 1

for signal in signals:
    if (cycle - 1) % 40 == 0:
        crt += "\n"
    crt += "#" if (cycle - 1) % 40 in (value - 1, value, value + 1) else " "

    if signal.startswith("noop"):
        cycle += 1
    else:
        if cycle % 40 == 0:
            crt += "\n"
        crt += "#" if cycle % 40 in (value - 1, value, value + 1) else " "
        cycle += 2
        value += int(signal.split()[1])

print("Part2 Answer:",crt)