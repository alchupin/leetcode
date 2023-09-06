# sorted list of numbers, return two numbers if sum exsists, empty list if it doesn't

def two_sum(num_list, target):
    left_pointer = 0
    right_pointer = len(num_list) - 1
    
    while not left_pointer == right_pointer:
        if num_list[left_pointer] + num_list[right_pointer] == target:
            return [num_list[left_pointer], num_list[right_pointer]]
        if num_list[left_pointer] + num_list[right_pointer] < target:
            left_pointer += 1
        if num_list[left_pointer] + num_list[right_pointer] > target:
            right_pointer -= 1
    return []


num_list = [-8, -3, 2, 4, 5, 5, 15, 22, 35]
target = -1

print(two_sum(num_list, target))