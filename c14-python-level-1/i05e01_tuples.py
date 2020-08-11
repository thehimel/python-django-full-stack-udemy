"""
Tuples are ordered collection of elements which are immutable by index.
In list, we can mutate any element by the index. But in tuple, we can't.
That's the only difference between tuple and list.

Order is available. Thus, slicing in tuple works just like list.
"""

data = (1, 'a', 2)
print(data)

print(data[0])  # 1

# data[0] = '10'  # TypeError: 'tuple' object does not support item assignment

print(data[-1])  # 2
print(data[::-1])  # (2, 'a', 1) <- Reversed the tuple with slicing


# Named tuple
import collections

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])

items = [
    Item(10, 2), Item(29, 10), Item(5, 7),
    Item(5, 3), Item(5, 1), Item(24, 12)]

for item in items:
    print(item)

"""
Item(weight=10, value=2)
Item(weight=29, value=10)
Item(weight=5, value=7)
Item(weight=5, value=3)
Item(weight=5, value=1)
Item(weight=24, value=12)
"""

print(items[0].weight, items[0].value)  # 10 2
