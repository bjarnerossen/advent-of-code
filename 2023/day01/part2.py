# one, two, three, four, five, six, seven, eight, and nine 
# also count as valid "digits".
import regex as re

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

total = 0

for line in open("input.txt", "r"):
    matches = re.findall(
            r'(one|two|three|four|five|six|seven|eight|nine|\d)'
            , line
            , overlapped=True
    )

    first = matches[0]
    last = matches[-1]

    if len(first) > 1:
        first = numbers.index(first) + 1

    if len(last) > 1:
        last = numbers.index(last) + 1

    total += int(f"{first}{last}")
        
print('Part 2:', total)