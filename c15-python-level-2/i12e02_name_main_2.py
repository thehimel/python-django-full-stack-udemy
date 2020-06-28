import i12e01_name_main_1 as one

one.get_view()

print("Top level two.")

if __name__ == '__main__':
    print("Two is called directly.")
else:
    print("Two is imported.")


"""
python i12e02_name_main_2.py

Output:
Top level one.
One is imported.
View of one.
Top level two.
Two is called directly.
"""
