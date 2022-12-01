with open("input.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

elves = [] 
count = 0
for item in data:
    if item == '':
        elves.append(count)
        count = 0
    
    else:
        count += int(item)

first_elf = sum(sorted(elves,reverse=1)[:1])
first_three_elves = sum(sorted(elves,reverse=1)[:3])

# Part1
print(f"The Elf with the most Calories, carries: {first_elf} calories.")
# Part2
print(f"The top three Elves carrying the most Calories, carry: {first_three_elves} calories.")