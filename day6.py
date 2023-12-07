file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "") for i in data]
tline, dline = data[0], data[1]
# times = [int(i.strip()) for i in tline.split(":")[1].strip().split()]
# dists = [int(i.strip()) for i in dline.split(":")[1].strip().split()]

times = [int(tline.split(":")[1].replace(" ", ""))]
dists = [int(dline.split(":")[1].replace(" ", ""))]

print(f"Times={times}")
print(f"Dists={dists}")

numways = 1
races = len(times)
for race in range(races):
    hold_times = speeds = range(times[race]+1)
    tleft = [times[race] - t for t in hold_times]
    d = [tleft[i] * speeds[i] for i in range(len(tleft))]
    wins = sum([i > dists[race] for i in d])
    numways *= wins

print(f"NumWays={numways}")
