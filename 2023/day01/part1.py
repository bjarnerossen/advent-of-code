total = 0
for line in open("input.txt", "r"):
    for value in line:
        if value.isdigit():
            total += int(value)*10
            break
    for value in line[::-1]:
        if value.isdigit():
            total += int(value)
            break
        
print('Part 1:', total)