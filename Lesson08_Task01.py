"""
Lesson08 Task01.

Given the list of integers ( positive , negative, zeros)

Find max multiplication of three values in list
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
Output: Max value = "2016". Nums are: (-7, 12, -24)
"""

from itertools import permutations

l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

copy_l1 = l1[:]

# remove all 0s from copy_l1
l1_no_0 = [x for x in copy_l1 if x != 0]

# create different combinations
combinations = list(permutations(l1_no_0, 3))

# multiple first 3 values for each combination and find max
mult = []
for val in combinations:
    mult_result = val[0] * val[1] * val[2]
    mult.append(mult_result)

# find first 3 values that return max multiplication result
max_value = max(mult)
max_nums = combinations[mult.index(max_value)]

print(f'Max value = "{max_value}". Nums are: {max_nums}')
