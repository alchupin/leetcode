file_path = 'input.txt'
file_path = '/home/alexey/study/leetcode-1/ALGO_4/warm_up/j_sum_of_two_products.txt'

# на интервале [n/a, n/b] должно быть целое число

def can_collect_sum(n, a, b):
    if (a == 1 or b == 1):
        return 'YES'
    if a + b == n:
        return 'YES'
    if a == b and n % a == 0:
        return 'YES'
    x = (n // a)
    y = (n // b)
    if x - y >= 1:
        return 'YES'
    return 'NO'

with open(file_path, 'r') as f:
    f.readline()
    for line in f.readlines():
        n, a, b = map(int, line.split())
        print(can_collect_sum(n, a, b))