def count_digits(num):
    digits_list = [0] * 10
    while num > 0:
        digits_list[num % 10] += 1
        num //=  10
    return digits_list

print(count_digits(2587672346))

def is_digit_permutation(num_1, num_2):
    return count_digits(num_1) == count_digits(num_2)


print(is_digit_permutation(2345, 3532))