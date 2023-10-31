def get_not_minimum(l):
    if len(l) <= 2:
        return 'NOT FOUND'
    min_num = l[0]
    for i in range(1, len(l)):
        if l[i] < min_num:
            return min_num
        elif l[i] > min_num:
            return l[i]
    return 'NOT FOUND'

file_path = 'input.txt'
file_path = '/home/alexey/study/leetcode-1/ALGO_4/warm_up/data/a_not_minimum_data.txt'


with open(file_path, 'r') as f:
    nums_len, queue_number = map(int, f.readline().split())
    nums = list(map(int, f.readline().split()))
    for line in f.readlines():
        queue = tuple(map(int, line.split()))
        L = queue[0]
        R = queue[1] + 1
        l = nums[L:R]
        print(get_not_minimum(l))
