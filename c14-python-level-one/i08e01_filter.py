"""
class filter
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.

"""


def is_even(num):
    return num % 2 == 0


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(is_even(4))  # True

evens = list()
for num in numbers:
    if is_even(num):
        evens.append(num)
print(evens)  # [0, 2, 4, 6, 8]


# Let's do the same thing with filter()
result = list(filter(is_even, numbers))
print(result)  # [0, 2, 4, 6, 8]

# If you don't use the list, it will return a generator.
result_without_list = filter(is_even, numbers)
print(result_without_list)  # <filter object at 0x000001854AB4E508>
