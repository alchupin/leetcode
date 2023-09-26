# https://leetcode.com/problems/length-of-last-word/

def get_length(s: str) -> int:
    return len(s.strip().split(' ')[-1])

s = "   fly me   to   the moon  "
print(get_length(s))