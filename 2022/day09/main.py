def motions(moves, length):
    pos = [[0, 0] for _ in range(length)]
    visited = set()
    
    for move in moves:
        dir, steps = move.split()
        for _ in range(int(steps)):
            visited.add(tuple(pos[-1]))
            if dir == "D":
                pos[0][1] += 1
            elif dir == "U":
                pos[0][1] -= 1
            elif dir == "L":
                pos[0][0] -= 1
            elif dir == "R":
                pos[0][0] += 1
            for i, ((hx, hy), (tx, ty)) in enumerate(zip(pos, pos[1:])):
                if abs(hx - tx) > 1:
                    tx += 1 if hx > tx else -1
                    if abs(hy - ty) > 0:
                        ty += 1 if hy > ty else -1
                elif abs(hy - ty) > 1:
                    ty += 1 if hy > ty else -1
                    if abs(hx - tx) > 0:
                        tx += 1 if hx > tx else -1
                pos[i + 1][0] = tx
                pos[i + 1][1] = ty

    visited.add(tuple(pos[-1]))

    return len(visited)



with open("input.txt") as f:
    moves = f.read().splitlines()
    print("Part1 Answer:", motions(moves, 2))
    print("Part2 Answer:", motions(moves, 10))