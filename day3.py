import string
import re

file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "").split(",")[0] for i in data]

n, m = len(data), len(data[0])
symbols = list(string.punctuation.replace(".", ""))
numerics = [str(i) for i in range(10)]


def contains_symbol(schematic, start, end):
    window = schematic[start: end+1]
    if any(s in window for s in symbols):
        return True


def is_overlap(interval1, interval2):
    len_overlap = min(interval1[1], interval2[1]) - max(interval1[0], interval2[0])
    if len_overlap >= 0:
        return True
    return False


def get_numerics(schematic, start, end):
    res = []
    num_matches_schematic = [(_m.start(), _m.end()-1) for _m in re.finditer(r"(\d+)", schematic)]
    for match_schematic in num_matches_schematic:
        if is_overlap(match_schematic, [start, end]):
            num_schematic = int(schematic[match_schematic[0]: match_schematic[1]+1])
            res.append(num_schematic)
    return res


partsum = 0
gear_ratio_sum = 0
for i in range(n):
    # Find parts
    num_matches = [(m.start(), m.end()) for m in re.finditer(r"(\d+)", data[i])]
    for match in num_matches:
        x, y = max(0, match[0]-1), min(match[1], n-1)
        num = int(data[i][match[0]: match[1]])
        if (
                contains_symbol(data[i], x, y) or
                (i > 0 and contains_symbol(data[i-1], x, y)) or
                (i < n-1 and contains_symbol(data[i+1], x, y))
        ):
            partsum += num  # found part
        else:
            # print(f"Line {i}; IGNORING {num} -- NOT A PART")
            pass

    # Find gears
    gear_matches = [ind for ind, el in enumerate(data[i]) if el == "*"]
    for match in gear_matches:
        x, y = max(0, match-1), min(match+1, n-1)
        gear_numerics = []
        gear_numerics += get_numerics(data[i], x, y)
        if i > 0:
            gear_numerics += get_numerics(data[i-1], x, y)
        if i < n-1:
            gear_numerics += get_numerics(data[i+1], x, y)
        if len(gear_numerics) == 2:
            gear_ratio = gear_numerics[0] * gear_numerics[1]
            gear_ratio_sum += gear_ratio

print(f"PartSum = {partsum}")
print(f"GearRatioSum = {gear_ratio_sum}")
