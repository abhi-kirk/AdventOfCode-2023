with open("input.txt", "r") as f:
    data = f.readlines()

data = [i.replace("\n", "") for i in data]
nums_alpha = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
              "six": 6, "seven": 7, "eight": 8, "nine": 9,
              "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
              "6": 6, "7": 7, "8": 8, "9": 9}
res = 0


def get_cal_value(cal_corrupted):
    n = len(cal_corrupted)

    left_map = {}
    for num in nums_alpha:
        left_index = cal_corrupted.find(num)
        if 0 <= left_index < n:
            left_map[left_index] = num
    left_num = nums_alpha[left_map[min(left_map)]]

    right_map = {}
    for num in nums_alpha:
        right_index = cal_corrupted.rfind(num)
        if 0 <= right_index < n:
            right_map[right_index] = num
    right_num = nums_alpha[right_map[max(right_map)]]

    return 10 * left_num + right_num


for i in range(len(data)):
    cal = get_cal_value(data[i])
    print(f"i={i}; data={data[i]}; cal={cal}")
    res += cal

print(res)
