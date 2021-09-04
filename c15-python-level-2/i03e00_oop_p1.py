# Built-in classes
print(type([]))
print(type(()))


# User defined class
class Sample:
    pass


x = Sample()

# Get the type of the object.
print(type(x))

# Check if the object is an instance of the class.
print(isinstance(x, Sample))
