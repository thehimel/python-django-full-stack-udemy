"""
Important Note:
Dictionaries are the implementation of hash-map in Python.
Thus, dictionaries doesn't have any order.
"""

person = {
    'name': 'Smith',
    'age': 22,
    'profession': 'Student'
}

print(person)  # {'name': 'Smith', 'age': 22, 'profession': 'Student'}
print(person['name'].upper())  # SMITH


food_menu = {
    'bfast': ['fruits', 'breads', 'milk'],
    'lunch': 'as usual',
    'dinner': {
        'starter': ['cheese ball', 'paneer kabab'],
        'main': ['rice', 'curry', 'salad'],
        'desert': ['sweet', 'ice cream']
    }
}

print(food_menu)

# Access an item
print(food_menu['bfast'])  # ['fruits', 'breads', 'milk']
print(food_menu['bfast'][0])  # fruits
print(food_menu['dinner']['main'])  # ['rice', 'curry', 'salad']
print(food_menu['dinner']['main'][2])  # salad

# Adding an item
food_menu['snacks'] = ['tea', 'biscuits']
print(food_menu)  # {... 'snacks': ['tea', 'biscuits']}


# Check the existence of an item
if 'bfast' in food_menu.keys():
    print('bfast is available in the food menu.')
