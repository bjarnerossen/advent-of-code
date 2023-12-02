#Part 1

# "(" --> +1
# ")" --> -1

with open("input.txt") as f:
    data = [line.strip() for line in f]
    floor = 0
    for line in data:
        for i, parenthesis in enumerate(line):
            if parenthesis == '(':
                floor += 1
            elif parenthesis == ")":
                floor -= 1

            if floor == -1:
                #Part 2
                print(f"Part 2: Santa is in the basement on position {i+1}")
                break
            else:
                continue

#Part 1
print(f"Part 1: Santa is on floor {floor}.")