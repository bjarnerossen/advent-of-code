import re
from collections import defaultdict

# Part1
with open("input.txt") as file:
    crates, moves = file.read().split("\n\n")

stacks = defaultdict(list)
for crate in crates.split('\n')[::-1][1:]:
  for i, c in enumerate(crate[1::4]):
    if c != ' ':
      stacks[i + 1].append(c)
    
moves = re.findall(r"move (\d+) from (\d+) to (\d+)", moves)
moves = [map(int, move) for move in moves]
moves = [[qty, from_, to_] for qty, from_, to_ in moves]

for qty, from_ , to_ in moves:
    for _ in range(qty):
        crates = stacks[from_].pop()
        stacks[to_].append(crates)

answer1 = ""
for stack in stacks.values():
    answer1 += stack[-1]   

# Part2
for qty, from_ , to_ in moves:
    stacks[to_].extend(stacks[from_][-qty:])
    stacks[from_] = stacks[from_][:-qty]

answer2 = ""
for stack in stacks.values():
    answer2 += stack[-1]   


print("Part1 Answer:", answer1)
print("Part2 Answer:", answer2)