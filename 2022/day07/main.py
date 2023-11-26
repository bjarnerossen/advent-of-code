from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)
paths = [] 
with open("input.txt") as file:

    for line in file.read().splitlines():
        if line.startswith("$ cd"):
            dir = line[5:]
            if dir == "..":
                paths.pop()
            else:
                paths.append(dir)
        elif line.startswith("$ ls"):
            continue
        else:
            try:
                dirs["/".join(paths)] += int(line.split()[0])
            except ValueError:
                pass

for dir in sorted(dirs.keys(), key=lambda x: x.count("/"), reverse=True):
    dirs["/".join(dir.split("/")[:-1])] += dirs[dir]

answer_1 = sum(x for x in dirs.values() if x <= 100.000)

free_storage = 70_000_000 - dirs["/"]
needed = 30_000_000 - free_storage
answer_2 = min(y for y in dirs.values() if y > needed)

print("Answer Part1:", answer_1)
print("Answer Part1:", answer_2)
