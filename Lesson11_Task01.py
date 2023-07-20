"""
Lesson11 Task01.

write generator function that has as input some range value and chunk_size
produces output as lists with len == chunk size
Example:
Call:  chunk_generator(range(11), chunk_size=3) ->
Output:  [0, 1, 2]
         [3, 4, 5]
         [6, 7, 8]
         [9, 10]
"""


def chunk_generator(range_value, chunk_size):
    """Create lists with chunks size from a given range."""
    iterator = iter(range_value)
    while True:
        lst = []
        try:
            for _ in range(chunk_size):
                lst.append(next(iterator))
            yield lst
        except StopIteration:
            if lst:
                yield lst
            break


range_value = range(11)
chunk_size = 3
for lst in chunk_generator(range_value, chunk_size):
    print(lst)
