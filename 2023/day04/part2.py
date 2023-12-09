import re

with open('input.txt') as file:
    cards = file.read().splitlines()

card_counter = {}
for card_number in range(1, len(cards) + 1):
    card_counter[card_number] = 1

for card_number, card in enumerate(cards):
    left, right = card.split(':')[1].split('|')
    winning_numbers = {int(number) for number in re.findall(r'\d+', left)}
    my_numbers = {int(number) for number in re.findall(r'\d+', right)}
    num_matches = len(winning_numbers & my_numbers)

    for won_copies in range(card_number+1, card_number+1 + num_matches):
        card_counter[won_copies] += card_counter[card_number]

print(sum(card_counter.values()))