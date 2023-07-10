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

l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

copy_l1 = l1[:]

# check if the length of the list contains at least 3 val
if len(copy_l1) < 3:
    print('At least 3 values should be in the input')
else:
    max_mult = copy_l1[0] * copy_l1[1] * copy_l1[2]
    max_nums = (copy_l1[0], copy_l1[1], copy_l1[2])

    # find the maximum multiplication among three values
    for i in range(len(copy_l1) - 2):
        for j in range(i + 1, len(copy_l1) - 1):
            for k in range(j + 1, len(copy_l1)):
                mult = copy_l1[i] * copy_l1[j] * copy_l1[k]
                if mult > max_mult:
                    max_mult = mult
                    max_nums = (copy_l1[i], copy_l1[j], copy_l1[k])

    print(f'Max value = "{max_mult}". Nums are: {max_nums}')
