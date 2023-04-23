"""
Inheritance:
The way of creating a class from another class.
Derived class is created from the base class.

Derived class has all the characteristics of the base class.
Method overriding is also allowed.
"""


class Animal:
    def __init__(self):
        print("Animal created.")

    def who_are_you(self):
        print("I am an animal.")

    def eat(self):
        print("Your animal is eating.")


my_animal = Animal()  # Animal created.
my_animal.eat()  # Your animal is eating.


# Deriving Dog class from base class Animal.
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created.")

    def bark(self):
        print("Woof! Woof!")

    # Method overriding
    def eat(self):
        print("Your Dog is eating.")


my_dog = Dog()  # Dog created.
my_dog.bark()  # Woof! Woof!
my_dog.who_are_you()  # I am an Animal.
my_dog.eat()  # Your Dog is eating.
