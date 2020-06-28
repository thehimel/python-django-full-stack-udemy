def add(x, y):
    print(x + y)


try:
    add(5, 'string')

# If exception
except TypeError:
    print("Caught a TypeError.")

else:
    print("No exception.")

finally:
    print("Finally always runs.")


# ---------------------------------------
try:
    add(5, 'string')

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
