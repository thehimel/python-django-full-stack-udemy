"""
Imporant Note:
Strings are immutable.
str = "Hello World"
str[2] = "Z"  # This is not possible.

But you can replace the string.
str = "Something new"  # This is possible

Slicing
-------
Slice: [start_index : end_index : step_size]
Works like: for(i=start_index, i<end_index, i+=step_size)

Slice: string[2:30:2]
Works like: for(i=2; i<30; i+=2)


If you want to go upto the end_index, add 1 to it.
Slice: [start_index : end_index+1 : step_size]
Works like: for(i=start_index, i<=end_index, i+=step_size)

Slice: string[2:30+1:2]
Works like: for(i=2; i<=30; i+=2)
"""


# String declaration
str1 = "Hello World"
print(str1)

str2 = 'Hello World'
print(str2)

str3 = "I'm a Doctor"
print(str3)


# Operations
string = "abcdef"
print(string.upper())
print(string.lower())
print(string.capitalize())  # Capitalize the first letter only

string = "Hello World"
print(string.split())  # ['Hello', 'World'] <- By default splits on space

string = "Dog, Cat, Tiger"
print(string.split(', '))  # ['Dog', 'Cat', 'Tiger']
print(string.split(', ')[0])  # Dog

string = "abcdef"
print(string[0])  # 'a'
print(string[-1])  # 'f' - Last character


# Slicing
string = "abcdef"
print(string[2:])  # cdef <- From index 2 to last
print(string[:4])  # abcd <- for(i=0; i<4; i++) <- From 0, upto less than 4
print(string[2: 4])  # cd <- for(i=2; i<4; i++) <- From 2, upto less than 4
print(string[2: 4+1])  # cde <- for(i=2; i<=4; i++) <- From to upto 4

print(string[:])  # abcdef <- Returns the whole string
print(string[::])  # abcdef <- Returns the whole string

print(string[::1])  # Returns string with step size 1 = Whole string
print(string[::2])  # ace <- Returns characters after every 1 element

print(string[::-1])  # fedcba <- Reversed the string
print(string[::-2])  # fdb <- In reverse order, after every 1 element


# Format
print("1st item is {} and 2nd item is {}".format("Cake", "Ice Cream"))
print("1st item is {x} and 2nd item is {y}".format(x="Cake", y="Ice Cream"))
print("1st item is {y} and 2nd item is {x}".format(x="Cake", y="Ice Cream"))
print("1st item is {x} and 2nd item is also {x}".format(x="Cake"))

x, y = "Cake", "Ice Cream"
# print("1st item is {x} and 2nd item is {y}".format(x, y)) <- Not possible
print("1st item is {x} and 2nd item is {y}".format(x=x, y=y))

print(f"1st item is {x} and 2nd item is {y}")  # Best way
