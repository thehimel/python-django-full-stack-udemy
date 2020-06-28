the_list = [1, 2, 3, 4, 5]
print(the_list)

print(the_list[0])  # 1
print(the_list[-1])  # 5
print(the_list[::-1])  # [5, 4, 3, 2, 1] <- Reverse

the_list[0] = 99
print(the_list)  # [99, 2, 3, 4, 5] <- Replaced item on the index

the_list = ['a', 'b', 1, 2, 3, 'Hello', ['Dog', 'Cat'], 'Cream']
print(the_list)  # Different types of data allowed. But same type recommended.


# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0])  # 1
print(matrix[0][2])  # 3


# List comprehension
new_list = [row[0] for row in matrix]  # [1, 4, 7]
print(new_list)

numbers = [1, 2, 3, 4]
squares = [num**2 for num in numbers]
print(squares)  # [1, 4, 9, 16]


# Creating a list of size 10 with 0 in every position
new_list = [0 for _ in range(10)]
print(new_list)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(len(new_list))  # 10

new_list = [i for i in range(10)]
print(new_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# List operations
the_list = [1, 2, 3, 4, 5]
the_list.append(10)  # Appends at the end
print(the_list)  # [1, 2, 3, 4, 5, 10]

letters = ['a', 'b', 'c']
the_list.append(letters)  # Appends the list
print(the_list)  # [1, 2, 3, 4, 5, 10, ['a', 'b', 'c']]

the_list = [1, 2, 3, 4, 5]
the_list.extend(letters)  # Extends the original list
print(the_list)  # [1, 2, 3, 4, 5, 'a', 'b', 'c']


the_list = [1, 2, 3, 4, 5, 10]
item = the_list.pop()  # Removes and returns the last item
print(item)  # 10
print(the_list)  # [1, 2, 3, 4, 5]

item = the_list.pop(0)  # Remvoes and returns the item from the given index
print(item)  # 1
print(the_list)  # [2, 3, 4, 5]

the_list = [1, 2, 3, 4, 5]
the_list.reverse()  # Reversed the list in-place
print(the_list)  # [5, 4, 3, 2, 1]

the_list = [55, 21, 47, 85, 45, 85]
the_list.sort()  # Sorts the list in-place
print(the_list)  # [21, 45, 47, 55, 85, 85]

the_list = [40, 20, 30, 10, 50]
sorted_list = sorted(the_list)  # Returns the sorted list, doesn't mutate.
print(the_list)  # [40, 20, 30, 10, 50]
print(sorted_list)  # [10, 20, 30, 40, 50]
