"""
Class has attributes and methods.
Attributes are characteristics of the class. And methods are the actions
performed by the class.

If Dog is a class, color is an attribute and run is a method.

In the bellow example Circle is a class.
pi is the class object attribute. It doesn't require the self keyword
before it to initialize. We call it by Circle.pi because its
same for all circles.

radius, color are the attributes. Attributes can be set or get just by
calling them. Methods can also be created to as setter and getter.

area, set_radius, and get_radius are the methods of class Circle.

During a attribute call, no paranthesis is required. While calling a
method, the paranthesis is a must.
"""


class Circle():
    # Class object attribute
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

    def area(self):
        return Circle.pi * self.radius**2


my_circle = Circle()
# Getting the attribute
print(my_circle.color)  # White

print(my_circle.radius)  # 10

# Getting the attribute through the method
print(my_circle.get_radius())  # 10
print(my_circle.area())  # 314.0

# During initialization, if you mention the attribute name,
# like radius=25, order is not necessary.
yellow_circle = Circle(radius=25, color="Yellow")
print(yellow_circle.color)  # Yellow
print(yellow_circle.area())  # 1962.5

yellow_circle = Circle(color="Yellow", radius=25)
print(yellow_circle.color)  # Yellow
print(yellow_circle.area())  # 1962.5

# If you don't mention the attribute name, order is important.
red_circle = Circle(33, "Red")
print(red_circle.color)  # Red
print(red_circle.area())  # 3419.46