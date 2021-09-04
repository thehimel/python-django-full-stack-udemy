"""
True, 1, Value - All are treated as True

False, 0, None - All are treated as False
"""

a = True
a = 1
a = "Something"

if a:
    print(a)


b = False
b = 0

c = None
# Doesn't run as None is treated as False
if c:
    print("C1", c)

# Runs as None is treated as False
if not c:
    print("C2", c)
