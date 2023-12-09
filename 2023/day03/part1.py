import re
from collections import defaultdict

with open("test.txt") as file:
    data = file.readlines()

# Finding coordinates for the symbols
symbols = dict()
for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char not in "1234567890.":
                symbols[(row, col)] = char
    
print(symbols)

# checking if a number has a neighboor containing a symbol
gears = defaultdict(list)
part_numbers_sum = 0
for row, line in enumerate(data):
    for match in re.finditer(r"\d+", line):
        # print(match)
        for (s_row, s_col), char in symbols.items():
            # print(s_row, s_col, char)
            # checking the start and end coordinates of each number
            start_position = match.start() - 1
            end_position = match.end()
            is_within_row_range = start_position <= s_row <= end_position

            # checking the columns above and below each number
            col_lower_bound = col - 1
            col_upper_bound = col + 1
            is_within_col_range = col_lower_bound <= s_col <= col_upper_bound

            if is_within_row_range and is_within_col_range:
                num = int(match.group())
                part_numbers_sum += num
                break

print(f"Sum of part numbers: {part_numbers_sum}")