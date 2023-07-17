"""
Lesson10 Task01.

open input2.txt file
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
    with open('input2.txt', 'r') as input_fh:
        data = input_fh.read()
        pattern = (
            r'(?<=[^A-Z])'  # lookbehind for non-uppercase letter
            r'(?P<before>[A-Z]{3})'  # three uppercase letters before
            r'(?P<element>[a-z])'  # lowercase element
            r'(?P<after>[A-Z]{3})'  # three uppercase letters after
            r'(?=[^A-Z])'  # lookahead for non-uppercase letter
        )
        matches = re.findall(pattern, data)
        print('Result:')
        for match in matches:
            print(
                match[0], match[1], match[2], '-> matches ',
                match[1], sep='',
            )

except Exception as g_exc:
    print(g_exc)
