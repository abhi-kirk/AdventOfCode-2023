from itertools import accumulate, combinations


file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()


def expand(axis, scale):
    empty = [scale - 1] * (max(axis) + 1)
    for n in axis:
        empty[n] = 0
    add = list(accumulate(empty))
    for n in axis:
        yield n + add[n]


def pathsum(galaxies):
    return sum(abs(bx - ax) + abs(by - ay)
               for (ax, ay), (bx, by) in combinations(galaxies, 2))


galaxies = [(x, y) for y, line in enumerate(data)
                   for x, char in enumerate(line) if char == '#']
print(pathsum(zip(*(expand(axis, 2) for axis in zip(*galaxies)))))
print(pathsum(zip(*(expand(axis, 1000000) for axis in zip(*galaxies)))))
