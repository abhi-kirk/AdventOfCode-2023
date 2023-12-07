from collections import Counter

file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "") for i in data]

n = len(data)
hands_bids = {}
for i in range(n):
    hand = data[i].split()[0]
    bid = int(data[i].split()[1])
    hands_bids[hand] = bid

types = {"high": 0, "one": 1, "two": 2, "three": 3, "full": 4, "four": 5, "five": 6}
SORT_ORDER = "J23456789TQKA"


def get_handtype(handstr):
    hfreq = Counter(list(handstr))
    vals = sorted(hfreq.values())
    if len(hfreq) == len(handstr):
        htype = "high"
    elif len(hfreq) == 1:
        htype = "five"
    elif vals == [1, 4]:
        htype = "four"
    elif vals == [2, 3]:
        htype = "full"
    elif vals == [1, 1, 3]:
        htype = "three"
    elif vals == [1, 2, 2]:
        htype = "two"
    else:
        htype = "one"
    return htype


def handleJ(handstr):
    strength = {}
    labels = list(SORT_ORDER)[1:]
    for label in labels:
        handstr_replaced = handstr.replace("J", label)
        strength[handstr_replaced] = types[get_handtype(handstr_replaced)]
    max_strength = max(strength.values())
    for s in strength:
        if strength[s] == max_strength:
            handstr = s
            break
    return handstr


hands_types = {}
for i in range(n):
    hand_orig = data[i].split()[0]
    if "J" in hand_orig:
        hand_mod = handleJ(hand_orig)
        hands_types[hand_orig] = get_handtype(hand_mod)
    else:
        hands_types[hand_orig] = get_handtype(hand_orig)


hands_ranks = {}
rank = 1
for t in types:
    thands = []
    for key, val in hands_types.items():
        if val == t:
            thands.append(key)
        else:
            continue
    if len(thands) > 1:
        thands = [list(i) for i in thands]
        thands_sorted = sorted(thands, key=lambda h: [SORT_ORDER.index(c) for c in h])
        thands_sorted = ["".join(i) for i in thands_sorted]
        for th in thands_sorted:
            hands_ranks[th] = rank
            rank += 1
    elif len(thands) == 1:
        hands_ranks[thands[0]] = rank
        rank += 1

winnings = 0
for hand in hands_bids:
    winnings += hands_bids[hand] * hands_ranks[hand]

print(f"Winnings={winnings}")
