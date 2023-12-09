import re
from collections import defaultdict

with open("input.txt") as file:
    data = file.read().split("\n")

# Finding coordinates for the symbols
symbols = dict()
for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char not in "1234567890.":
                symbols[(x, y)] = char
    
# print(symbols)

# checking if a number has a neighboor containing a symbol
part_numbers_sum = 0
for y, line in enumerate(data):
    for match in re.finditer(r"\d+", line):
        # print(match)
        for (s_x, s_y), char in symbols.items():
            # checking the start and end coordinates of each number
            start_position = match.start() - 1
            end_position = match.end()
            is_within_row_range = start_position <= s_x <= end_position

            # checking the columns above and below each number
            col_lower_bound = y - 1
            col_upper_bound = y + 1
            is_within_col_range = col_lower_bound <= s_y <= col_upper_bound

            if is_within_row_range and is_within_col_range:
                num = int(match.group())
                part_numbers_sum += num
                break

print(part_numbers_sum)
