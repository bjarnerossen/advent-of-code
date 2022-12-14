# When comparing two values
# first val -> left
# second val -> right

# if both int -> lower first, bigger second
# if both vals are lists -> first val of left list, first of second list
## if the left list runs out of items -> inputs in correct order
## if the right list runs out of items -> inputs not in correct order

# if 1 val int -> convert int ot a list
from functools import cmp_to_key

def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            return (a > b) - (a < b)
        return compare([a], b)
    if type(b) == int:
        return compare(a, [b])
    for aa, bb in zip(a, b):
        if r := compare(aa, bb):
            return r
    return compare(len(a), len(b))


with open("input.txt") as f:
    data = f.read()
    part1, part2 = 0, 1

    for i, pairs in enumerate(data.split("\n\n")):
        a, b = map(eval, pairs.splitlines())
        if compare(a, b) == -1:
            part1 += i + 1

    pairs = [eval(p) for p in data.splitlines() if p]
    pairs.append([[2]])
    pairs.append([[6]])
    pairs.sort(key=cmp_to_key(compare))
    for i, p in enumerate(pairs):
        if p == [[2]]:
            part2 *= i + 1
        if p == [[6]]:
            part2 *= i + 1

    print("Answer Part1:", part1)
    print("Answer Part2:", part2)