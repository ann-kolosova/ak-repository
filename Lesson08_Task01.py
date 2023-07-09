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

# sort the list in descending order by absolute value
sorted_list = sorted(copy_l1, key=abs, reverse=True)

# check if the length of the list is less than 3
if len(sorted_list) < 3:
    print('At least 3 values should be in the input')
else:
    max_mult = sorted_list[0] * sorted_list[1] * sorted_list[2]
    max_nums = (sorted_list[0], sorted_list[1], sorted_list[2])

    # find the maximum multiplication among three values
    for i in range(len(sorted_list) - 2):
        for j in range(i + 1, len(sorted_list) - 1):
            for k in range(j + 1, len(sorted_list)):
                mult = sorted_list[i] * sorted_list[j] * sorted_list[k]
                if mult > max_mult:
                    max_mult = mult
                    max_nums = (sorted_list[i], sorted_list[j], sorted_list[k])

    print(f'Max value = "{max_mult}". Nums are: {max_nums}')
