digit = ''
print_buffer = ''

with open("dataset_3363_2.txt", 'r+') as text_file:
    for letter in text_file:
        for i in range(len(letter)):

            char = letter[i]
            if char.isdigit():
                digit = digit + char
                if i == len(letter) - 1:
                    for k in range(int(digit)):
                        print_buffer += letter_tmp

            else:
                if len(digit) == 0:
                    pass

                else:
                    for k in range(int(digit)):
                        print_buffer += letter_tmp
                        digit = ''

                letter_tmp = letter[i]


# print(print_buffer)
# out_file = open("string.txt", 'w')
# out_file.write(print_buffer)
