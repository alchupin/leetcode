from collections import Counter
from typing import Iterable


def count_ch_in_str(s):
    result = ''
    dct = {}
    max_count = 0
    for ch in s:
        if ch not in dct:
            dct[ch] = 0
        dct[ch] += 1
        if dct[ch] > max_count:
            max_count = dct[ch]
            result = ch
    return result, max_count

s = 'dukgskflagwiefgbanlsygfdhilsduwjdfukyrgfhsdhufhwiurgfhsldfushirgufhjlseuf'
# print(count_ch_in_str(s))

s_c = Counter(s).most_common()[0]
# print(s_c)

def most_common_ch(s: str) -> Iterable:
    max_ = 0
    result_dict = {}
    for ch in s:
        if ch not in result_dict:
            result_dict[ch] = 0
        result_dict[ch] += 1
        if result_dict[ch] > max_:
            max_ = result_dict[ch]
            result = ch
    return result, max_

print(most_common_ch(s))