def add(x, y):
    print(x + y)


try:
    add(5, "string")

# If exception
except TypeError:
    print("Caught a TypeError.")

else:
    print("No exception.")

finally:
    print("Finally always runs.")


# ---------------------------------------
try:
    add(5, "string")

except Exception:
    print("Caught an exception.")

else:
    print("No exception.")

finally:
    print("Finally always runs.")


# ---------------------------------------
try:
    add(5, 10)

except Exception:
    print("Caught an exception.")

else:
    print("No exception.")

finally:
    print("Finally always runs.")


# ---------------------------------------
try:
    add(150, 150)

except Exception:
    print("Caught an exception.")

finally:
    print("Finally always runs.")

# ---------------------------------------
"""
Author: Himel Das

Output:
12
No exception is caught.
Execution completed.
"""

try:
    result = 10 + 2
    print(result)
except TypeError:
    print("Caught TypeError.")
except NameError:
    print("Caught NameError.")
else:
    print("No exception is caught.")
finally:
    print("Execution completed.")

# ---------------------------------------
"""
Author: Himel Das

Output:
Caught TypeError.
Execution completed.
"""

try:
    result = 10 + "2"
    print(result)
except TypeError:
    print("Caught TypeError.")
except NameError:
    print("Caught NameError.")
else:
    print("No exception is caught.")
finally:
    print("Execution completed.")

# ---------------------------------------
"""
Author: Himel Das

Output:
Caught NameError.
Execution completed.
"""

try:
    result = 10 + 2
    print(result_not_exists)
except TypeError:
    print("Caught TypeError.")
except NameError:
    print("Caught NameError.")
else:
    print("No exception is caught.")
finally:
    print("Execution completed.")

# ---------------------------------------
"""
Author: Himel Das

Output:
Caught TypeError.
Execution completed.

Note: There exists 2 exceptions in the code. However, when the first one is
caught, the program shows only the first exception.
"""

try:
    result = 10 + "2"
    print(result_not_exists)
except TypeError:
    print("Caught TypeError.")
except NameError:
    print("Caught NameError.")
else:
    print("No exception is caught.")
finally:
    print("Execution completed.")
