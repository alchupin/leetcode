def binary_search(l_sorted, match):
    left = 0
    right = len(l_sorted)-1
    attempts = 0
    while left <= right:
        attempts += 1
        curr = (right + left) // 2
        if match == l_sorted[curr]:
            return curr, attempts
        if match < l_sorted[curr]:
            right = curr
        else:
            left = curr
    return -1, attempts

l = [i for i in range(1, 101)]
print(l)
num = 75
print(binary_search(l, num))