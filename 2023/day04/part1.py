# separated by a vertical bar (|):
    # a list of winning numbers and 
    # then a list of numbers you have.
import re

with open("input.txt") as cards:
    total_points = 0

    for card in cards:
        left, right = card.split(':')[1].split('|')
        winning_numbers = {int(number) for number in re.findall(r'\d+', left)}
        my_numbers = {int(number) for number in re.findall(r'\d+', right)}

        matches_count = len(set(winning_numbers) & set(my_numbers))

        points = 2 ** (matches_count - 1) if matches_count > 0 else 0
        total_points += points
    
    print(total_points)
