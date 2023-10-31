from math import gcd

file_path = 'input.txt'
file_path = '/home/alexey/study/leetcode-1/ALGO_4/warm_up/b_sum_two_fractions.txt'

with open(file_path, 'r') as f:
    a, b, c, d = map(int, f.readline().split())
    n = (a * d) + (c * b)
    m = b * d
    nm_gcd = gcd(n, m)
    n = int(n / nm_gcd)
    m = int(m / nm_gcd)
    print(n, m)
