from math import lcm

file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "") for i in data]

dirs = data[0]
nodes = data[2:]


def get_dir(dir_word, node_dirs):
    if dir_word == "L":
        return node_dirs[0]
    return node_dirs[1]


def create_map(map_data):
    n = len(map_data)
    hmap = {}
    endA = []
    for i in range(n):
        key = map_data[i].split("=")[0].strip()
        if key.endswith("A"):
            endA.append(key)
        val = map_data[i].split("=")[1].strip().replace("(", "").replace(")", "").replace(" ", "").split(",")
        hmap[key] = val
    return hmap, endA


dmap, nodes_end_A = create_map(nodes)
print(f"Starting Nodes={nodes_end_A}")


def num_steps_toZ(start_node):
    curr_node = start_node
    steps = i = 0
    while True:
        if i == len(dirs):
            i = 0
        d = dirs[i]
        next_node = get_dir(d, dmap[curr_node])
        steps += 1
        i += 1
        if next_node.endswith("Z"):
            break
        curr_node = next_node
    return steps


num_steps = []
for nodeA in nodes_end_A:
    num_steps.append(num_steps_toZ(nodeA))

print(f"StepsTo..Z={lcm(*num_steps)}")
