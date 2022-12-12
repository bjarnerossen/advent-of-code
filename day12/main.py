# lowercase lettes
# a -> lowest 
# b -> next-lowest
# ... elevation level

# UPPERCASE letters
# S -> current position
# E (z) -> location with best signal, elevation z
# S (a) -> a elevation

# Parse the input and store it in a two-dimensional list
with open("input.txt", "r") as f:
    data = f.read()

visited = [[False] * 1000 for i in range(1000)]

heightmap = [list(s) for s in data.split("\n")]
r = len(heightmap)
c = len(heightmap[0])


for i in range(r):
    for a in range(c):
        if heightmap[i][a] == "S":
            start = (i, a, 0)
            heightmap[i][a] = "a"
        elif heightmap[i][a] == "E":
            end = (i, a)
            heightmap[i][a] = "z"

queue = []
queue.append(start)
visited[start[0]][start[1]] = True

while queue:
    head = queue.pop(0)
    x, y, s = head

    if (x, y) == end:
        print("Least steps:", s)
        exit()

    for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        newx = x + dx
        newy = y + dy

        if 0 <= newx and newx < r and 0 <= newy and newy < c:
            if not visited[newx][newy] and ord(heightmap[newx][newy]) <= ord(heightmap[x][y]) + 1:
                queue.append((newx, newy, s + 1))
                visited[newx][newy] = True