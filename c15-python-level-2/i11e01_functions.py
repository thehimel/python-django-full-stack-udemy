def view():
    print("Sky is blue.")


watch = view
watch()  # Sky is blue.


def world():
    print("The world is beautiful.")

    def ocean():
        print("Ocean is nice.")

    return ocean


# Returns the function ocean()
my_world = world()  # The world is beautiful.
my_world()  # Ocean is nice.
