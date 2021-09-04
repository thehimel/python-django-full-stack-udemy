"""
Suppose there is a simple function gift(). Now we need to add some code
before and/or after the gift() function. The decorator() takes the gift(),
wrap_gift() adds some codes before and after the gift(), and decorator()
returns wrap_gift().

So, when we run gift = decorator(gift), gift() has
been changed and wrapped by the wrap_gift() through the decorator().

Then when we call gift() after the decoration. We get,
Wrapping the gift().
This is a gift.
gift() has been wrapped.
"""


def decorator(gift):
    def wrap_gift():
        print("Wrapping the gift().")
        gift()
        print("gift() has been wrapped.")

    return wrap_gift


def gift():
    print("This is a gift.")


gift = decorator(gift)

gift()
