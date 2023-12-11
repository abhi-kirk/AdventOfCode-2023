import copy
from collections import deque
import sys

sys.setrecursionlimit(2000)
file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "") for i in data]
grid = [list(i) for i in data]
grid_original = copy.deepcopy(grid)
# print(f"Grid={grid}")

# Part 1: BFS
m, n = len(grid), len(grid[0])
S = [None, None]
for i in range(m):
    for j in range(n):
        if grid[i][j] == "S":
            S = [i, j]
print(f"Start={S}")

queue = deque()
queue.append((S[0], S[1]))
grid[S[0]][S[1]] = 0

pipes = {
    "S": {"up": ["|", "F", "7"], "down": ["|", "J", "L"],
          "left": ["-", "F", "L"], "right": ["-", "J", "7"]},
    "-": {"up": [], "down": [],
          "left": ["L", "F", "-"], "right": ["-", "J", "7"]},
    "|": {"up": ["|", "F", "7"], "down": ["|", "J", "L"],
          "left": [], "right": []},
    "F": {"up": [], "down": ["|", "J", "L"],
          "left": [], "right": ["-", "7", "J"]},
    "J": {"up": ["|", "F", "7"], "down": [],
          "left": ["-", "L", "F"], "right": []},
    "7": {"up": [], "down": ["|", "J", "L"],
          "left": ["-", "F", "L"], "right": []},
    "L": {"up": ["|", "F", "7"], "down": [],
          "left": [], "right": ["-", "J", "7"]},
}


def is_conn(current_tile, next_tile, direction):
    possible_tiles = pipes[current_tile][direction]
    if len(possible_tiles) > 0 and next_tile in possible_tiles:
        return True
    return False


max_dist = 0
while queue:
    i, j = queue.popleft()
    distance = grid[i][j]
    max_dist = max(max_dist, distance)
    dirs = {
        "up": [i - 1, j],
        "down": [i + 1, j],
        "left": [i, j - 1],
        "right": [i, j + 1]
    }
    for d in dirs:
        di, dj = dirs[d][0], dirs[d][1]
        dir_invalid = di < 0 or di >= m or dj < 0 or dj >= n
        if dir_invalid or not is_conn(current_tile=grid_original[i][j], next_tile=grid[di][dj], direction=d):
            continue
        grid[di][dj] = distance + 1
        queue.append((di, dj))

print(f"MaxDist={max_dist}")


# Part 2: DFS


def dfs(i, j, t):
    global wentToBoundary
    if i < 0 or j < 0 or i >= m or j >= n or not isinstance(grid[i][j], str):
        return 0
    grid[i][j] = -1
    t = 1
    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
        wentToBoundary = True
        return 0
    dirs = [
        [i - 1, j],
        [i + 1, j],
        [i, j - 1],
        [i, j + 1],
    ]
    for d in dirs:
        di, dj = d[0], d[1]
        t += dfs(di, dj, t)
    return t


def in_loop(posx, posy):
    vertical_pipes_crossed = 0
    for y in range(posy):
        if grid[posx][y] >= 0:
            vertical_pipes_crossed += 1
    if vertical_pipes_crossed % 2 == 1:
        return True
    return False


flood_fills = {}
for row in range(m):
    for col in range(n):
        if isinstance(grid[row][col], str):
            wentToBoundary = False
            tiles = dfs(row, col, 0)
            if not wentToBoundary:
                flood_fills[(row, col)] = tiles

tiles_enclosed = 0
for fill in flood_fills:
    if in_loop(posx=fill[0], posy=fill[1]):
        tiles_enclosed += flood_fills[fill]

print(f"TilesEnclosed={tiles_enclosed}")
