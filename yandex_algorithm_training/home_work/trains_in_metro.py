def count_times(a, b, n, m,):
    min_1 = (n - 1) * a + n
    max_1 = (n - 1) * a + n + 2 * b
    min_2 = (m - 1) * b + m
    max_2 = (m - 1) * b + m + 2 * b
    
    min_time = max(min_1, min_2)
    max_time = min(max_1, max_2)
    if max_time < min_time:
        return -1
    else:
        return min_time, max_time