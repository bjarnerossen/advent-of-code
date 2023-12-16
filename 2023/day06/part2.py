import math
import re

data = open('input.txt').read().replace(' ', '')
race_duration = int(re.findall(r'\d+', data)[0])
record_distance = int(re.findall(r'\d+', data)[1])

wins = 0
for hold_duration in range(14, race_duration-13):
    speed = hold_duration
    distance = (race_duration - hold_duration) * speed
    if distance > record_distance:
        wins += 1


print(wins)