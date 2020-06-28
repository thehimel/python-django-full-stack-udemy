global_str = "This is a global string."


def my_function():
    local_str = "This is a local string."
    print(locals())  # {'local_str': 'This is a local string.'}
    print(globals())  # {'global_str': 'This is a global string.', ... }


my_function()
