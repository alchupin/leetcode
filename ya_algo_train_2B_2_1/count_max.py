def count_max_in_list(l):
    max_number = 0
    count_max = 1
    for num in l:
        if num == max_number:
            count_max += 1
        elif num > max_number:
            max_number = num
            count_max = 1
    return count_max


l = [9, 7, 9, 9, 0]
print(count_max_in_list(l))