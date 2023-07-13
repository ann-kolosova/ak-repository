"""
Lesson09 Task01.

# write script that will read "input.txt" file
and find there all characters from english alphabet
# collect these characters and their positions in file
# after info collected this info as text write
to "output.txt" file in such format
# ####################
# <first found letter> -> pos1
# <next_letter> -> pos2
# <next_letter -> pos3
# etc
# #######################
"""

import re

try:
    with open('input.txt', 'r') as input_txt:
        data = input_txt.read()
        eng_letters = re.findall('[a-zA-Z]', data)
        letter_pos = [(letter, data.index(letter)) for letter in eng_letters]
        print(letter_pos)

    with open('output.txt', 'w') as output_txt:
        for letter, position in letter_pos:
            output_txt.write(f'<{letter}> -> pos{position}\n')

except Exception as e:
    print(e)
