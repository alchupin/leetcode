l = [4, 22, 35, 8, 13, 7, 19, 22, 35, 13]

def find_max_num(seq: list[int]) -> int:
    max_num =  float('-inf')
    for num in seq:
        if num > max_num:
            max_num = num
    return max_num

# print(find_max_num(l))


def two_max_nums(seq: list[int]) -> tuple[int]:
    if seq[0] > seq[1]:
        max_max, max_min = seq[0], seq[1]
    else:
        max_min, max_max = seq[0], seq[1]
    for i in range(2, len(seq)):
        if seq[i] >= max_max:
            max_min = max_max
            max_max = seq[i]
        elif max_min < seq[i] < max_max:
            max_min = seq[i]
    return max_max, max_min

# print(two_max_nums(l))