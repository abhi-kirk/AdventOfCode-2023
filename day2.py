import re

file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()
data = [i.replace("\n", "") for i in data]


def get_color_nums(game_str_input):
    res = {"red": 0, "blue": 0, "green": 0}
    for color in res:
        color_num = re.findall(rf"(\d+) {color}", game_str_input)
        if len(color_num) > 0:
            color_num = color_num[0]
            res[color] = int(color_num)
    return res


max_nums = {"red": 12, "blue": 14, "green": 13}
idsum = 0
powersum = 0
for i in range(len(data)):
    fewest_nums = {"red": 0, "blue": 0, "green": 0}
    game_str = data[i]
    game = int(re.findall(r"Game (\d+):.*", game_str)[0])
    game_possible = True
    game_iters = game_str.split(":")[1].strip().split(";")
    for j in range(len(game_iters)):
        subgame = game_iters[j]
        colors_num = get_color_nums(subgame)
        subgame_str = f"game={game}; subgame={j}; {colors_num}"
        for c in colors_num:
            if colors_num[c] > fewest_nums[c]:
                fewest_nums[c] = colors_num[c]
            if colors_num[c] > max_nums[c]:
                game_possible = False
                # print(f"NOT POSSIBLE: {subgame_str}")
    if game_possible:
        idsum += game
    powersum += fewest_nums["red"] * fewest_nums["blue"] * fewest_nums["green"]

print(f"idsum = {idsum}")
print(f"powersum = {powersum}")
