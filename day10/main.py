with open("input.txt") as f:
    signals = f.read().splitlines()

    x = 1
    cycles = {"20": 0, "60": 0, "100": 0, "140": 0, "180": 0, "220": 0}

    cycle = 0 
    for signal in signals:
        if signal != "noop":
            for i in range(2):
                cycle += 1
                # print(f"cycle:{cycle}, val:{x}")
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

            
        if signal == "noop":
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

        # print(f"cycle:{cycle}, val:{x}")

# print(cycles)
print("Part1 Answer:", sum(value for value in cycles.values()))