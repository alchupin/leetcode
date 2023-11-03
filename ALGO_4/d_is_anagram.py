s1 = input()
s2 = input()
d1 = {}
d2 = {}
if not len(s1) == len(s2):
    print('NO')
for ch in s1:
    if ch in d1:
        d1[ch] += 1
    else:
        d1[ch] = 0
for ch in s2:
    if ch in d2:
        d2[ch] += 1
    else:
        d2[ch] = 0
if d1 == d2:
    print('YES')
else:
    print('NO')