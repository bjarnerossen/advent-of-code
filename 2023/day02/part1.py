with open("input.txt") as games:
    possible_ids = []

    for game in games:
        game_info = game.split(': ')
        game_id = int(game_info[0].split()[1])
        subsets = game_info[1].split('; ')

        valid_game = True

        for subset in subsets:
            limits = {"red": 12, "green": 13, "blue": 14}
            cubes = subset.split(", ")
            for cube in cubes:
                count, color = cube.split()
                if int(count) > limits[color]:
                    valid_game = False
                    break
                limits[color] -= int(count)
            if not valid_game:
                break
        
        if valid_game:
            possible_ids.append(game_id)

print("Sum of possible IDs:", sum(possible_ids))