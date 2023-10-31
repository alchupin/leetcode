file_path = 'input.txt'
file_path = '/home/alexey/study/leetcode-1/ALGO_4/warm_up/i_valid_parentheses.txt'

def is_valid_parentheses(s):
    if s == '':
        return 'yes'
    stack = []
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for p in s:
        if p in pairs:
            stack.append(p)
        elif len(stack) == 0 or p != pairs[stack.pop()]:
            return 'no'
    if len(stack) == 0:
        return 'yes'
    return 'no'

with open(file_path, 'r') as f:
    s = f.readline().strip()
    print(is_valid_parentheses(s))