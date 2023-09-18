def words_in_text(dictionary, text):
    extended_dict = set(dictionary)
    result = []
    for word in dictionary:
        for pos_to_del in range(len(word)):
            extended_dict.add(word[:pos_to_del] + word[pos_to_del+1:])
    for word in text.split():
        if word in extended_dict:
            result.append(word) 
    return result


test_dict = ['cat', 'dog', 'fly', 'ant', 'elephant']
text = 'The dg flys away. elephan lives in Africa.'

print(words_in_text(test_dict, text))