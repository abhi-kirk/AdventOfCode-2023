import copy
from collections import deque
from tqdm import tqdm


file = "test.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "") for i in data]
data = [list(i) for i in data]


def number_galaxies(univ):
    m, n = len(univ), len(univ[0])
    count = 1
    for i in range(m):
        for j in range(n):
            if univ[i][j] == "#":
                univ[i][j] = str(count)
                count += 1
    return univ


def expand_rows(univ):
    m, n = len(univ), len(univ[0])
    empty = n * ["."]
    i = 0
    while i < m:
        if all(v == "." for v in univ[i]):
            univ.insert(i+1, empty)
            i += 1
            m = len(univ)
        i += 1
    return univ


def shortest_distance(univ, galaxy1, galaxy2_list):
    # BFS
    res = {}
    m, n = len(univ), len(univ[0])
    queue = deque()
    queue.append((galaxy1[0], galaxy1[1]))
    univ[galaxy1[0]][galaxy1[1]] = 0
    while queue:
        i, j = queue.popleft()
        distance = univ[i][j]
        if [i, j] in galaxy2_list:
            res[(i, j)] = distance
        dirs = [
            [i-1, j],
            [i+1, j],
            [i, j-1],
            [i, j+1],
        ]
        for d in dirs:
            di, dj = d[0], d[1]
            if di < 0 or di >= m or dj < 0 or dj >= n or isinstance(univ[di][dj], int):
                continue
            univ[di][dj] = distance + 1
            queue.append((di, dj))
    return res


def get_subspace(univ, galaxy1, galaxy2):
    g1_val, g2_val = univ[galaxy1[0]][galaxy1[1]], univ[galaxy2[0]][galaxy2[1]]
    start_row = min(galaxy1[0], galaxy2[0])
    start_col = min(galaxy1[1], galaxy2[1])
    end_row = max(galaxy1[0], galaxy2[0]) + 1
    end_col = max(galaxy1[1], galaxy2[1]) + 1
    univ_mod = [i[start_col: end_col] for i in univ[start_row: end_row]]

    galaxy1_new, galaxy2_new = [None, None], [None, None]
    for i in range(len(univ_mod)):
        if g1_val in univ_mod[i]:
            galaxy1_new[0] = i
            galaxy1_new[1] = univ_mod[i].index(g1_val)
        if g2_val in univ_mod[i]:
            galaxy2_new[0] = i
            galaxy2_new[1] = univ_mod[i].index(g2_val)
    return univ_mod, galaxy1_new, galaxy2_new


# Expand Universe
data = number_galaxies(data)
data = expand_rows(data)
data = list(map(list, zip(*data)))
data = expand_rows(data)
data = list(map(list, zip(*data)))

# Get List of Galaxies
galaxies = []
for row in range(len(data)):
    for col in range(len(data[0])):
        element = data[row][col]
        if element != ".":
            galaxies.append({
                element: [row, col]
            })
print(f"NumGalaxies={len(galaxies)}")

# Shortest Distance Between Galaxies
num_gal = len(galaxies)
sum_distances = 0
for g1 in tqdm(range(num_gal-1)):
    g1_loc = list(galaxies[g1].values())[0]
    g2_list = list(range(g1+1, num_gal))
    g2_loc_list = [list(galaxies[i].values())[0] for i in g2_list]
    g1_distances = shortest_distance(univ=copy.deepcopy(data), galaxy1=g1_loc, galaxy2_list=g2_loc_list)
    sum_distances += sum(g1_distances.values())
print(f"SumDistances={sum_distances}")
