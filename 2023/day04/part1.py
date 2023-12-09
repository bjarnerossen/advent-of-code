# separated by a vertical bar (|):
    # a list of winning numbers and 
    # then a list of numbers you have.
with open("input.txt") as cards:
    total_points = 0

    for card in cards:
        winning_numbers, your_numbers = card.split(" | ")
        winning_numbers = winning_numbers.split()
        your_numbers = your_numbers.split()

        matches = set(winning_numbers) & set(your_numbers)
        matches_count = len(matches)

        points = 2 ** (matches_count - 1) if matches_count > 0 else 0
        total_points += points
    
    print(total_points)
