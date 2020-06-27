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
