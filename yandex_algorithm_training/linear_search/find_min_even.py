def find_min_even(seq: list[int]) -> int:
    min_num = float('inf')
    flag = False
    for num in seq:
        if num % 2 == 0 and num < min_num:
            flag = True
            min_num = num
    return min_num if flag else -1

# print(find_min_even([1, 3, 5]))
