"""
Special methods:
__init__: To initialize the object.

__str__: To return the string representation. Must return a single string.

__len__: Return a value representing the length of the object.

__del__: To delete an object.

Special methods must contain double underscores before and after the name.
"""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        s = f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
        return s

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f"{self.title} by {self.author} is deleted.")


my_book = Book("Python", "Smith", 250)
print(my_book)  # Title: Python, Author: Smith, Pages: 250
print(len(my_book))  # 250
del my_book  # Python by Smith is deleted.

# print(my_book)  # NameError: name 'my_book' is not defined
