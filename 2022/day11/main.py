from collections import defaultdict
from math import lcm, prod


ops = [
    lambda l: l * 17,
    lambda l: l * l,
    lambda l: l + 7,
    lambda l: l + 4,
    lambda l: l + 5,
    lambda l: l + 6,
    lambda l: l * 13,
    lambda l: l + 2,
]
divs = [2, 7, 13, 5, 3, 19, 11, 17]
if_trues = [2, 0, 7, 4, 1, 1, 3, 4]
if_falses = [6, 2, 6, 5, 5, 0, 7, 3]


def solve(num_rounds, part1):
    monkeys = [
        [85, 79, 63, 72],
        [53, 94, 65, 81, 93, 73, 57, 92],
        [62, 63],
        [57, 92, 56],
        [67],
        [85, 56, 66, 72, 57, 99],
        [86, 65, 98, 97, 69],
        [87, 68, 92, 66, 91, 50, 68],
    ]
    i = 0

    lcm_divs = lcm(*divs)
    inspected = defaultdict(int)
    for _ in range(num_rounds):
        for i, (monkey, op, div, if_true, if_false) in enumerate(
            zip(monkeys, ops, divs, if_trues, if_falses)
        ):
            while monkey:
                item = monkey.pop()
                inspected[i] += 1
                new = op(item) % lcm_divs
                if part1:
                    new //= 3
                monkeys[if_false if new % div else if_true].append(new)
    return prod(sorted(inspected.values())[-2:])


# Part 1
print("Answer Part1:",solve(20, True))
# Part 2
print("Answer Part2:",solve(10_000, False))