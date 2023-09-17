words = ['autumn', 'winter', 'spring', 'summer', 'snow', 'rain', ]

def find_shotest_words(seq: list[str]) -> list[str]:
    min_length = len(seq[0])
    for word in seq:
        if len(word) < min_length:
            min_length = len(word)
    result_list =  []
    for word in seq:
        if len(word) == min_length:
            result_list.append(word)
    return ' '.join(result_list)

# print(find_shotest_words(words))


def find_shotest_words_inf(seq: list[str]) -> list[str]:
    min_length = float('inf')
    for word in seq:
        if len(word) < min_length:
            min_length = len(word)
    result_list =  []
    for word in seq:
        if len(word) == min_length:
            result_list.append(word)
    return ' '.join(result_list)

print(find_shotest_words_inf(words))


