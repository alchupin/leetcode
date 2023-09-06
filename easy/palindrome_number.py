# https://leetcode.com/problems/palindrome-number/description/

def check_if_palindrome(num):
    return str(num) == str(num)[::-1]


def check_if_palindrome(num):
    if num < 0:
        return False
    
    new = 0
    orig = num
    while num:
        num, d = divmod(num, 10)
        new = new * 10 + d
    return new == orig

print(check_if_palindrome(121))