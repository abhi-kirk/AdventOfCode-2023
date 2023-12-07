import re

file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "").split(",")[0] for i in data]
hmap = {}


def card_value(num_matches):
    if num_matches == 0:
        return 0
    val = 1
    for _ in range(1, num_matches):
        val *= 2
    return val


def insert_hmap(keys):
    if isinstance(keys, int):
        keys = [keys]
    for key in keys:
        if key in hmap:
            hmap[key] += 1
        else:
            hmap[key] = 1


total_points = 0
for card in data:
    card_id = re.findall(r"Card\s+(\d+): .*", card)
    if len(card_id) > 0:
        card_id = int(card_id[0])
    else:
        print(f"Error with Card: {card}")
        continue
    insert_hmap(card_id)
    contents = card.split(":")[1].strip()
    card_nums = [int(i) for i in contents.split("|")[0].strip().split()]
    have_nums = [int(i) for i in contents.split("|")[1].strip().split()]

    num_wins = 0
    for num in have_nums:
        if num in card_nums:
            num_wins += 1
    card_points = card_value(num_wins)
    total_points += card_points

    won_cards_ids = [card_id + 1 + i for i in range(num_wins)]
    # print(f"WonCards = {won_cards_ids}")

    all_won_cards_ids = hmap[card_id] * won_cards_ids
    insert_hmap(all_won_cards_ids)
    # print(hmap)

print(f"TotalPoints = {total_points}")
print(f"TotalScratchCards = {sum(hmap.values())}")
