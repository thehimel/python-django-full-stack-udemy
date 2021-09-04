# Conditional Statements
a = 10
b = 20

if a == 10:
    print("a is 10")

print("b is 20" if b == 20 else "b is not 20")


if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

x = 10
y = 20
z = 30

if y < x:
    print("y is less than x")
elif x < y:
    print("x is less than y")
else:
    print("Arrived at the else part")
