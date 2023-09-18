def get_ch_count(ch, num):
    if num > 1:
        return ch + str(num)
    return ch

def RLE(s):
    result_list = []
    curr_ch = s[0]
    ch_count = 1
    for ch in s[1:]:
        if ch == curr_ch:
            ch_count += 1
        else:
            result_list.append(get_ch_count(curr_ch, ch_count))
            curr_ch = ch
            ch_count = 1
    result_list.append(get_ch_count(curr_ch, ch_count))
    return ''.join(result_list)

s = 'aaaaaaaaaabbbsdhglwlijjjjjjsssslllllwwwkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'

print(RLE(s))
