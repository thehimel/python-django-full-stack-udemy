from django import template


register = template.Library()


@register.filter(name="add_before")  # Register with decorator (recommended).
def add_before(value, arg):
    """value: str, arg: str. Adds arg before value."""
    return str(arg) + str(value)  # Forcing the data type just to stay safe.


def subtract(value, arg):
    """value: int, arg: int. Subtract arg from value."""
    return int(value) - int(arg)  # Forcing the data type just to stay safe.


register.filter("subtract", subtract)  # Register by passing the function.
