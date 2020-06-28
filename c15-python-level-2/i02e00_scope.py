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


# Fetching the global
def get_global_var():
    print(x)  # 10


get_global_var()

# ----------------------------------
# Global
x = 20


def get_enclosing_local():
    x = 30

    def get_enclosing():
        print(x)  # 20


print(x)
