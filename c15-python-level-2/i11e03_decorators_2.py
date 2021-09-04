"""
gift = decorator(gift) can also be done by adding @decorator before gift().
It does the same job.

Decorator can be imagine in this way. Imagine a wedding ceremony.
We have few objects like stage, gate, car etc.
If we send this objects to the decorator, the decorator will wrap the object
and decorate it. And they will do it by adding some flowers and other
additional accessories with the main object.

The python decorator also works like that. It takes the function, with
a wrapper function it wraps the function and returns the wrapper function
so that the given function becomes a wrapped function.
"""


def decorator(gift):
    def wrap_gift():
        print("Wrapping the gift().")
        gift()
        print("gift() has been wrapped.")

    return wrap_gift


@decorator
def gift():
    print("This is a gift.")


gift()
