"""
class filter
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.

"""


def is_even(value):
    return value % 2 == 0


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(is_even(4))  # True

evens = list()
for num in numbers:
    if is_even(num):
        evens.append(num)
print(evens)  # [0, 2, 4, 6, 8]


# Let's do the same thing with filter()
evens = list(filter(is_even, numbers))
print(evens)  # [0, 2, 4, 6, 8]

# If you don't use the list, it will return a generator.
evens_without_list = filter(is_even, numbers)
print(evens_without_list)  # <filter object at 0x000001854AB4E508>


""" lambda """
# For x in numbers, lambda x such that x is divisible by 2
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [0, 2, 4, 6, 8]


def get_product(x, y):
    return x * y


print(get_product(5, 6))
