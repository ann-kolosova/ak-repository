"""
Lesson10 Task01.

open input.txt file
and find all small english letters that match such conditions:
target small letter round exactly with three capital english letters
on the left and on the right
Match examples:
sdTRYaUVKn  -> matches "a"
NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
zDFGbOPNq   -> matches "b"
Print Output as : "Result: "<your_found_human_readable_string">
"""

import re

try:
    with open('input.txt', 'r') as input_txt:
        data = input_txt.read()
        let = re.findall('(?<=[^A-Z])[A-Z]{3}[a-z][A-Z]{3}(?=[a-z])', data)
        print('Result:')
        for matches in let:
            print(f'{matches:>15} -> matches "{matches[3]}"\n')

except Exception as e:
    print(e)
