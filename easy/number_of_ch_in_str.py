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
print(count_ch_in_str(s))