def sort_words_list(word_list):
    word_dict = {}
    for word in word_list:
        word_key = ''.join(sorted(word))
        if word_key not in word_dict:
            word_dict[word_key] = []
        word_dict[word_key].append(word)
    return list(word_dict.values())


print(sort_words_list(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
