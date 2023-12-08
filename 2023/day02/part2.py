with open("input.txt") as games:
    cube_powers = []

    for game in games:
        game_info = game.split(': ')
        subsets = game_info[1].split('; ')
        
        limits = {"red": 0, "green": 0, "blue": 0}
        for subset in subsets:
            cubes = subset.split(", ")
            for cube in cubes:
                count, color = cube.split()
                if int(count) > limits[color]:
                    limits[color] = int(count)
        result = 1
        for value in limits.values():
            result *= value
        cube_powers.append(result)
    
    print(f"Sum of the power of sets: {sum(cube_powers)}")

        