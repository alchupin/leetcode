file_path = 'input.txt'
file_path = '/home/alexey/study/leetcode-1/ALGO_4/warm_up/data/e_average_level.txt'


def count_average_level(l):
    prefix_sum_list = get_prefix_sum_list(l)
    average_level_list = []
    for i in range(len(l)):
        average_level = 0
        average_level = get_left_sum(l, prefix_sum_list, i) + get_right_sum(l, prefix_sum_list, i)
        average_level_list.append(average_level)
    return average_level_list

def get_prefix_sum_list(l):
    prefix_sum = [0] * (len(l) + 1)
    for i in range(1, len(l)+1):
        prefix_sum[i] += l[i-1] + prefix_sum[i-1]
    return prefix_sum

def get_prefix_sum(prefix_sum_list, r, l):
    prefix_sum = prefix_sum_list[r] - prefix_sum_list[l]
    return prefix_sum

def get_left_sum(l, prefix_sum_list, element_number):
    rectangle = (element_number) * l[element_number] 
    prefix_sum = get_prefix_sum(prefix_sum_list, element_number+1, 0)
    left_sum = rectangle - prefix_sum
    return left_sum

def get_right_sum(l, prefix_sum_list, element_number):
    prefix_sum = get_prefix_sum(prefix_sum_list, len(l), element_number)
    diff = (len(l) - (element_number+1)) * l[element_number]
    right_sum = prefix_sum - diff
    return right_sum



with open(file_path, 'r') as f:
    f.readline()
    nums = list(map(int, f.readline().split()))
    levels = count_average_level(nums)
    for level in levels:
        print(level, end=' ')