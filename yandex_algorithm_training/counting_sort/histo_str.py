def print_histo_str(s):
    character_dict = {}
    for ch in s:
        if not ch in character_dict:
            character_dict[ch] = 0
        character_dict[ch] += 1
    s_sorted = ''.join(sorted(set(s)))
    print(character_dict)
    for i in range(max(character_dict.values()), 0, -1):
        for ch in s_sorted:
            print('#', end='') if i <= character_dict[ch] else print(' ', end='')
        print()
    print(s_sorted)
    
print(print_histo_str('Hello, world!!!!!!!'))
