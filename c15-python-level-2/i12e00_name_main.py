"""
if __name__ == '__main__':
    .. code ..

This is used to determine whether the python file is being called by it's
file name or it's imported.

In other programming languages, the main() must be called explicitly.
But in Python, whatever is written in the file, act like the main function
and it's called automatically.

Although if __name__ == '__main__' can be used as calling the main function for
clearification.
"""


def get_view():
    print("The sky is beautiful.")


if __name__ == '__main__':
    get_view()  # The sky is beautiful.
