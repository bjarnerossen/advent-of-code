## Opponent
# A: Rock
# B: Paper
# C: Scissor

## Me 
# X: Rock --> 1
# Y: Paper --> 2
# Z: Scissor --> 3

## Score
# Lost --> 0
# Draw --> 3
# Win --> 6



with open("input.txt", "r") as file:
    data = file.read().splitlines() 
    data = [line.split() for line in data]

print(data)