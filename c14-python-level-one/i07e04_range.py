num = list(range(10))
print(num)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num = list(range(0, 10))
print(num)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num = list(range(10, 20))
print(num)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

num = list(range(10, 20+1))
print(num)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

num = list(range(10, 20, 2))
print(num)  # [10, 12, 14, 16, 18]

num = list(range(10, 20+1, 2))
print(num)  # [10, 12, 14, 16, 18, 20]


# 0 1 2 3 4
for num in range(5):
    print(num, end=' ')
print()

# 0 1 2 3 4 5
for num in range(5+1):
    print(num, end=' ')
print()
