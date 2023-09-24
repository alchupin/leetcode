def print_histo_str(s):
    character_dict = {}
    for ch in s:
        if not ch in character_dict:
            character_dict[ch] = 0
        character_dict[ch] += 1
    s_sorted = sorted(character_dict.keys())
    max_count = max(character_dict.values())
    for i in range(max_count, 0, -1):
        for ch in s_sorted:
            print('#', end='') if i <= character_dict[ch] else print(' ', end='')
        print()
    print(''.join(s_sorted))
    
print_histo_str('Hello, world!')
