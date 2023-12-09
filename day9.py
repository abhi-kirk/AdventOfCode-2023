file = "input.txt"
with open(file, "r") as f:
    data = f.readlines()

data = [i.replace("\n", "") for i in data]


def get_diff_seq(seq):
    begs, ends = [seq[0]], [seq[-1]]
    while True:
        diff = []
        for i in range(len(seq)-1):
            diff.append(
                seq[i+1] - seq[i]
            )
        begs.append(diff[0])
        ends.append(diff[-1])
        if all(v == 0 for v in diff):
            break
        seq = diff
    return begs, ends


def extrap_forward(seq):
    _, diff_seq = get_diff_seq(seq)
    print(f"-->Seq={diff_seq}")
    diff_seq = diff_seq[::-1]
    prev = 0
    for i in range(len(diff_seq)):
        curr = diff_seq[i]
        pred = curr + prev
        prev = pred
    return pred


def extrap_backward(seq):
    diff_seq, _ = get_diff_seq(seq)
    print(f"-->Seq={diff_seq}")
    diff_seq = diff_seq[::-1]
    prev = 0
    for i in range(len(diff_seq)):
        curr = diff_seq[i]
        pred = curr - prev
        prev = pred
    return pred


res = 0
for history in data:
    history = [int(i) for i in history.split(" ")]
    print(f"History={history}")
    next_pred = extrap_backward(history)
    print(f"---->Pred={next_pred}")
    res += next_pred

print(f"\nSumExtrapolations={res}")
