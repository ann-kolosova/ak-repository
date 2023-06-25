"""
Lesson06 Task01.

we have two lists with equal or different size
ex. l1=[1,3,5,7]  l2=[1,4,5]
task:
create list that will store such values
list_target = [(1,1), (3,4), (5,5), (7,0)]
zero (0) is our default value that we set
if no such element by index was found in certain list.
code should work and vise versa
ex. l1=[1,4,5] l2=[1,3,5,7] input data should produce
list_target = [(1,1), (4,3), (5,5), (0,7)]
your solution should include comprehension constructions

Advices:
set of (list1 indexes union list2 indexes) could be helpful
to get larger indexes scope ( or use if-else)
dict as you remember has default value if key was not found d1.get(key, 0)
l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]
"""

l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]

([l1.append(0) for _ in range(len(l2) - len(l1))]
    if len(l1) < len(l2)
    else [l2.append(0) for _ in range(len(l1) - len(l2))])

list_target = list(zip(l1, l2))
print(list_target)
