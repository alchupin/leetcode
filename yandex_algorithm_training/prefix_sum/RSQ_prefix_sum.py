def make_prefix_sum_list(nums):
    prefix_sum_list = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix_sum_list[i] = prefix_sum_list[i - 1] + nums[i - 1]
    return prefix_sum_list


def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]