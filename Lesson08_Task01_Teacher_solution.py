"""
Lesson08 Task01. Teacher's solution.

Given the list of integers ( positive , negative, zeros)

Find max multiplication of three values in list
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
Output: Max value = "2016". Nums are: (-7, 12, -24)
"""

l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

c_l1 = l1[:]

# check if the length of the list contains at least 3 val
if len(c_l1) < 3:
    raise ValueError('At least 3 values should be in the input')

# sort values from min to max
c_l1.sort()

# 2variants of possible max multiplication
max1 = c_l1[0] * c_l1[1] * c_l1[-1]
max2 = c_l1[-3] * c_l1[-2] * c_l1[-1]

# compare and print max multiplication
if max1 > max2:
    print(f'Max value = {max1}. Nums are: {c_l1[0], c_l1[1], c_l1[-1]}')
else:
    print(f'Max value = {max2}. Nums are: {c_l1[-3], c_l1[-2], c_l1[-1]}')
