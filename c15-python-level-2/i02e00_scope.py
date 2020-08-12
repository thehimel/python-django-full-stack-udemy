"""
The scope rule in Python:
LEGB

Local
Enclosing Functions Local
Global
Built-in
"""

# Global
x = 10


def get_local_var():
    # Local
    x = 20
    print(x)  # 20


get_local_var()

# ----------------------------------

# Global
x = 10


def see_global():
    global x
    x = "Changed to 20"
    print(x)


see_global()

x = 10


def get_global():
    print(x)  # 10


get_global()

# ----------------------------------
# Global
x = 20


def get_enclosing_local():
    x = 30

    def get_enclosing():
        print(x)  # 20

    get_enclosing()


get_enclosing_local()
print(x)


# Best way to change a global variable

global_var = 'Initial'
print(global_var)  # Initial


def change_global(x):
    x = 'Changed'
    return x


global_var = change_global(global_var)
print(global_var)  # Changed
