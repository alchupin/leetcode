# https://leetcode.com/problems/add-binary/

def bin_sum(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

def bin_to_dec(num_bin):
    sum = 0
    for i in range(len(num_bin), 0, -1):
        power = len(num_bin) - i
        sum += int(num_bin[i-1]) * 2**(power)
    return sum

def dec_to_bin(num_dec):
    sum = ''
    while num_dec > 0:
        num_dec, remainder = divmod(num_dec, 2)
        sum = str(remainder) + sum
    return sum

def bin_sum_str(a, b):
    sum = dec_to_bin(bin_to_dec(a) + bin_to_dec(b))
    return sum

# a = "11"
# b = "1"
# print(bin_sum(a, b))


print(bin_to_dec('101'))
print(dec_to_bin(6))
print(bin_sum_str('10', '100'))
