"""
num -> height
0 -> shortest
9 -> tallest
"""

test = r"""
30373
25512
65332
33549
35390
"""

with open("input.txt") as f:
    data = f.read().splitlines()
    grid = [list(map(int, line)) for line in data]

# Part1
visibles = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        k = grid[i][j]

        if all(grid[i][x] < k for x in range(j)):
                visibles += 1

        elif all(grid[i][x] < k for x in range(j + 1, len(grid[i]))):
                visibles += 1
        
        elif all(grid[x][j] < k for x in range(i)):
                visibles += 1
        
        elif all(grid[x][j] < k for x in range(i + 1, len(grid))):
                visibles += 1

print(f"Part1 Answer:", visibles)


# Part2
scenic_score = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        k = grid[i][j]
        L = R = U = D = 0

        for x in range(j -1, -1, -1):
            L += 1
            if grid[i][x] >= k:
                break

        for x in range(j + 1, len(grid[i])):
            R += 1
            if grid[i][x] >= k:
                break

        for x in range(i -1, -1, -1):
            U += 1
            if grid[x][j] >= k:
                break

        for x in range(i + 1, len(grid)):
            D += 1
            if grid[x][j] >= k:
                break 

        max_sc = scenic_score = max(scenic_score, L * R * U * D)

print(f"Part2 Answer:", max_sc)