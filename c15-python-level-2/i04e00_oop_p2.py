"""
Class has attributes and methods.
Attributes are characteristics of the class. And methods are the actions
performed by the class.

If Dog is a class, color is an attribute and run is a method.

In the bellow example Circle is a class.
pi is the class object attribute. It doesn't require the self keyword
before it to initialize. We call it by `Circle.pi` because its
same for all circles.

radius, color are the attributes. Attributes can be set or get just by
calling them. Methods can also be created as setter and getter.

area, set_radius, and get_radius are the methods of class Circle.

my_circle, yellow_circle, red_circle are the objects of Circle class.

During an attribute call, no parenthesis is required. While calling a
method, the parenthesis is a must.

We can use a method without the parenthesis if we declare it as a property.
"""


class Circle:

    # Class Object Attribute (COA)
    pi = 3.14

    def __init__(self, radius=10, color="White"):
        self.radius = radius
        self.color = color

    # Setter
    def set_radius(self, new_radius):
        self.radius = new_radius

    # Getter
    def get_radius(self):
        return self.radius

    @property
    def area(self):
        return Circle.pi * self.radius ** 2


my_circle = Circle()
# Getting the attributes
print(my_circle.color)  # White
print(my_circle.radius)  # 10

# Getting the attribute through the method
print(my_circle.get_radius())  # 10
print(my_circle.area)  # 314.0

# During initialization, if you mention the attribute name,
# like radius=25, order is not necessary.
yellow_circle = Circle(radius=25, color="Yellow")
print(yellow_circle.color)  # Yellow
print(yellow_circle.area)  # 1962.5

yellow_circle = Circle(color="Yellow", radius=25)
print(yellow_circle.color)  # Yellow
print(yellow_circle.area)  # 1962.5

# If you don't mention the attribute name, order is important.
red_circle = Circle(33, "Red")
print(red_circle.color)  # Red
print(red_circle.area)  # 3419.46


"""Adding attribute after object creation"""
red_circle.origin = "North"
print(red_circle.origin)  # North
