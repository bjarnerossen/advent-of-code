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


# Part1
with open("input.txt") as file:
    data = file.read()
    data = data.split("\n")

score = 0

for line in data:
    opp, me = line.split()

    if me == "X":
        if opp == "C":
            score += 6
        if opp == "A":
            score += 3
        score += 1

    if me == "Y":
        if opp == "A":
            score += 6
        if opp == "B":
            score += 3
        score += 2

    if me =="Z":
        if opp == "B":
            score += 6
        if opp == "C":
            score += 3
        score += 3

# Part2
## Opponent
# A: Rock
# B: Paper
# C: Scissor

## Me 
# X: Loose 
# Y: Draw 
# Z: Win

# Rock --> 1
# Paper --> 2
# Scissor --> 3

## Score
# Lost --> 0
# Draw --> 3
# Win --> 6

score_2 = 0

for line in data:
    opp, me = line.split()

    if me =="X":
        if opp == "A":
            score_2 += 3
        if opp == "B":
            score_2 += 1
        if opp == "C":
            score_2 += 2

    if me == "Y":
        if opp == "A":
            score_2 += 4
        if opp == "B":
            score_2 += 5
        if opp == "C":
            score_2 += 6

    if me == "Z":
        if opp == "A":
            score_2 += 8
        if opp == "B":
            score_2 += 9
        if opp == "C":
            score_2 += 7
            
print(f"Part1 Answer:", score)
print(f"Part2 Answer:", score_2)
# scores = {
#         ("A", "B"): 4,
#         ("B", "X"): 1,
#         ("C", "X"): 7,
#         ("A", "Y"): 8,
#         ("B", "Y"): 5,
#         ("C", "Y"): 2,
#         ("A", "Z"): 3,
#         ("B", "Z"): 9,
#         ("C", "Z"): 6
#     }

# score = 0 

# with open("input.txt", "r") as file:
#     data = file.read().splitlines()
#     data = [line.split() for line in data]
#     final_data = [(opp, me) for opp, me in data]

    # for tuple in data:
    #     print(tuple)
        # for key_tuple, value in scores.items():
        #     if key_tuple == tuple:
        #         print(key_tuple, tuple)
        #         score += value

# print(score) 