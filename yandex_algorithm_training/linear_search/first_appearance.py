from math import inf


def find_first_appearance(l: list, num: int) -> int:
    result = -1
    for i in range(len(l)):
        if num == l[i] and result == -1:
            result = i
    return result

def find_last_appearance(l: list, num: int) -> int:
    result = -1
    for i in range(len(l)):
        if num == l[i]:
            result = i
    return result

l = [4, 22, 35, 8, 13, 77, 19, 22, 50, 13]
number = 22
print(find_first_appearance(l, number))
print(find_last_appearance(l, number))

def find_max_num(seq: list[int]) -> int:
    max_num =  float('-inf')
    for num in seq:
        if num > max_num:
            max_num = num
    return max_num

print(find_max_num(l))