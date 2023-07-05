"""
Lesson07 Task01.

Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

let's take that number always > 100 and only three digits
100 <= num <= 999
"""

num = 299

# convert int to string
digit = str(num)

# dictionary for hundreds and ones
hundreds_ones = {
    '0': '',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
}

# dictionary for tens_1
tens_1 = {
    '10': 'Ten',
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'Fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'Nineteen',
}

# dictionary for tens_2
tens_2 = {
    '0': '',
    '2': 'Twenty',
    '3': 'Thirty',
    '4': 'Forty',
    '5': 'Fifty',
    '6': 'Sixty',
    '7': 'Seventy',
    '8': 'Eighty',
    '9': 'Ninety',
}

result = [f'{hundreds_ones[digit[0]]} Hundred']

if digit[1] == '1':
    result.append(tens_1[digit[1:]])
else:
    result.append(tens_2[digit[1]])
    result.append(hundreds_ones[digit[2]])

print(' '.join(result))
