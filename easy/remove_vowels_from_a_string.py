# https://leetcode.com/problems/remove-vowels-from-a-string/

def remove_vowels(s):
    vowels = 'aeiou'
    result = ''
    for ch in s:
        if ch not in vowels:
            result += ch
    return result


def remove_vowels(s):
    vowels = set('aeiou')
    return ''.join(ch for ch in s if ch not in vowels)
    

print(remove_vowels('leetcodeisacommunityforcoders'))