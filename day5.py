import re

file = "test.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "") for i in data]

fline = data[0]
seeds = fline.replace("seeds: ", "").split(" ")
seeds = [int(i) for i in seeds]
seed_ranges = []
for i in range(len(seeds)):
    if i % 2 == 0:
        seed_start = seeds[i]
    else:
        seed_ranges.append([seed_start, seed_start+seeds[i]])

print(f"SeedRanges={seed_ranges}")
breakpoint()


def mapped_values(almanac, src_vals, it):
    src_ranges, dst_ranges = [], []
    while it < len(almanac) and "map" not in almanac[it] and len(almanac[it]) != 0:
        line = re.findall(r"(\d+) (\d+) (\d+)", almanac[it])[0]
        line = [int(i) for i in line]
        src_ranges.append([line[1], line[1] + line[2]])
        dst_ranges.append([line[0], line[0] + line[2]])
        it += 1
    dst_vals = []
    for s in src_vals:
        found = False
        for idx, src_range in enumerate(src_ranges):
            if src_range[0] <= s < src_range[1]:
                s_idx = s - src_range[0]
                dst_vals.append(dst_ranges[idx][0] + s_idx)
                found = True
                break
        if not found:
            dst_vals.append(s)
    return dst_vals, it+1


n = len(data)
i = 0
while i < n:
    if "seed-to-soil" in data[i]:
        i += 1
        soils, i = mapped_values(almanac=data, src_vals=seeds, it=i)
        print(f"Soil={soils}")
    if "soil-to-fertilizer" in data[i]:
        i += 1
        fertilizers, i = mapped_values(almanac=data, src_vals=soils, it=i)
        print(f"Fert={fertilizers}")
    if "fertilizer-to-water" in data[i]:
        i += 1
        waters, i = mapped_values(almanac=data, src_vals=fertilizers, it=i)
        print(f"Water={waters}")
    if "water-to-light" in data[i]:
        i += 1
        lights, i = mapped_values(almanac=data, src_vals=waters, it=i)
        print(f"Light={lights}")
    if "light-to-temperature" in data[i]:
        i += 1
        temps, i = mapped_values(almanac=data, src_vals=lights, it=i)
        print(f"Temp={temps}")
    if "temperature-to-humidity" in data[i]:
        i += 1
        humids, i = mapped_values(almanac=data, src_vals=temps, it=i)
        print(f"Humid={humids}")
    if "humidity-to-location" in data[i]:
        i += 1
        locs, i = mapped_values(almanac=data, src_vals=humids, it=i)
        print(f"Loc={locs}")
    i += 1

print(f"MinLocation={min(locs)}")
