max_number = 0
count_max = 0
while True:
    input_number = int(input())
    if not input_number == 0:
        if input_number == max_number:
            count_max += 1
        elif input_number > max_number:
            max_number = input_number
            count_max = 1
    else:
        break
print(count_max)