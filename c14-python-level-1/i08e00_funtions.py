"""
The docstring at the beginning of the function declaration,
provides an insight on what the function odes. If you hover over the
function name, or while calling the funtion later, the IDE will
show this docstring as the funtion details. It is helpful while working
in a large project.
"""


def get_product(x, y):
    result = x * y
    print(result)


get_product(2, 3)  # 6


def get_sum(x=10, y=20):
    """
    Returns the sum of 2 numbers
    """
    result = x + y

    return result


result = get_sum()
print(result)  # 30

result = get_sum(50, 60)
print(result)  # 110

print(type(result))  # <class 'int'>

if type(result) == int:
    print("Result is integer")


def divide(x, y):
    if type(x) == type(y) == type(10):
        return x / y
    else:
        return "All parameters must be integers."


print(divide(50, 5))  # 10.0
print(divide("50", 5))  # 'All parameters must be integers.'
