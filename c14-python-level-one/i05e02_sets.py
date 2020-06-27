"""
Set is unordered collection of unique elements.
An element can only be added once.
Additional addition won't raise an error. Just won't add an element twice.
"""

items = set()
items.add(1)
items.add(2)
items.add(3)
items.add(3)
items.add(3)
print(items)  # {1, 2, 3}

the_list = [10, 10, 10, 50, 50, 50, 60, 60, 60]
items = set(the_list)
print(items)
