numbers = [1, 2, 3, 4, 5, 6]

# 1 2 3 4 5 6
for num in numbers:
    print(num, end=' ')
print()


users = {
    'admin': 'Smith',
    'moderator': 'Nick',
    'editor': 'Angela'
}

# admin moderator editor
for user in users:
    print(user, end=' ')
print()

# admin moderator editor
for user in users.keys():
    print(user, end=' ')
print()

# Smith Nick Angela
for name in users.values():
    print(name, end=' ')
print()

# admin: Smith, moderator: Nick, editor: Angela,
for user in users:
    print(f'{user}: {users[user]}', end=', ')
print()


"""Tuple unpacking"""
fruits = [('Banana', 10), ('Apple', 20), ('Orange', 30)]

# Banana: 10, Apple: 20, Orange: 30,
for fruit, count in fruits:
    print(f'{fruit}: {count}', end=', ')
print()
