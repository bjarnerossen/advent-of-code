import re

data = open('input.txt').read().replace(' ', '')
race_duration = int(re.findall(r'\d+', data)[0])
record_distance = int(re.findall(r'\d+', data)[1])

def calculate_winning_options(race_duration, record_distance):
    wins = 0
    for hold_duration in range(1, race_duration):
        speed = hold_duration
        distance = (race_duration - hold_duration) * speed
        if distance > record_distance:
            wins += 1
    return wins

winning_options = calculate_winning_options(race_duration, record_distance)

print(winning_options)