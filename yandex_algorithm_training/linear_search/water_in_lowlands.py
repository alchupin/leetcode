def find_all_max(seq):    
    h_max = seq[0]
    result_list = [0]
    for i in range(len(seq)):
        if seq[i] > h_max:
            result_list = [i]
            h_max = seq[i]
        elif seq[i] == h_max:
            result_list.append(i)
    return result_list

l = [2, 1, 4, 2, 6, 2, 3, 4, 2, 6, 2, 1, 4, 2, 2, 6, 2, 4, 1, 2]
# print(find_all_max(l))


def find_max(seq):
    max_pos = 0
    for i in range(len(seq)):
        if seq[i] > seq[max_pos]:
            max_pos = i
    return max_pos


def count_from_left(seq):
    result_sum = 0
    current_max = seq[0]
    for i in range(len(seq)):
        if seq[i] > current_max:
            current_max = seq[i]
        elif seq[i] < current_max:
            result_sum += current_max - seq[i]
    return result_sum

def count_from_right(seq):
    result_sum = 0
    current_max = seq[-1]
    for i in range(len(seq)-1, 0, -1):
        if seq[i] > current_max:
            current_max = seq[i]
        elif seq[i] < current_max:
            result_sum += current_max - seq[i]
    return result_sum


l_left_1 = [2, 1, 4, 2, 6]
l_left_2 = [2, 3, 4, 2, 6]

# print(count_from_left(l_left_1))
# print(count_from_left(l_left_2))

l_right_1 = [6, 2, 4, 1, 1, 1, 2, 3]
# print(count_from_right(l_right_1))


def count_water_cubes(seq):
    max_pos = find_max(seq)
    result_sum = count_from_left(seq[0:max_pos+1]) + count_from_right(seq[max_pos:])
    return result_sum

l_with_one_maximum = [2, 1, 4, 2, 6, 2, 4, 1, 1, 1, 2, 3]


# print(count_water_cubes(l_with_one_maximum))
print(count_water_cubes(l))

