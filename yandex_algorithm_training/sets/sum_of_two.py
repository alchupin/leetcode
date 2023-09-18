def get_sum_of_two(nums, sum):
    num_set = set()
    for num in nums:
        if sum - num in num_set:
            return num, sum - num
        num_set.add(num)
    return -1

nums = [3, 5, 12, 15, 7, 2]
sum = 12

print(get_sum_of_two(nums, sum))