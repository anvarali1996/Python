# def add(a, b):
#     return a + b
# print(add(1, 4))

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1, 4, 7, 5, 5))


# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Dr.", "Anvarjon", "Saydulloyevich", "Sheraliev", "UZBEKISTAN")


# def print_address(**kwargs):
#     # for value in kwargs.values():
#     #     print(value)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address(street="Somewhere street",
#               city="Somehow",
#               state="Whre",
#               zip="12345")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    # print(f"{kwargs.get('apt')}")
    if "apt" in kwargs:
        print("THERE'S APT")
    else:
        print("NOOOOOO!!!!!!!!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("Dr", "Someone", "Noone",
               street="Somewhere",
               apt="1001",
               city="Where",
               zip="1234")