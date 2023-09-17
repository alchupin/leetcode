from math import inf

l = [4, 22, 35, 8, 13, 7, 19, 22, 35, 13]
number = 23

def find_first_appearance(l: list, num: int) -> int:
    for i in range(len(l)):
        if num == l[i]:
            return i
    return -1

# print(find_first_appearance(l, number))


def find_last_appearance(l: list, num: int) -> int:
    result = -1
    for i in range(len(l)):
        if num == l[i]:
            result = i
    return result

# print(find_last_appearance(l, number))
