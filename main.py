# def happy_birthday(name, age):
#     print(f"Happy birthday to you! {name}")
#     print(f"You're {age} years old")
#
# happy_birthday("Anvarjon", 25)
# happy_birthday("Nurmuhammad", 2)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}!")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
#
# display_invoice("anvarjon", 100.99, "01/02")

# def add(x, y):
#     z = x + y
#     return z
# def subtract(x, y):
#     z = x - y
#     return z
# def multiply(x, y):
#     z = x * y
#     return z
# def divide(x, y):
#     z = x / y
#     return z
#
#
# def add(x, y):
#     z = x + y
#     return z
#
#
# print(add(1, 2))
# print(subtract(8 , 2))
# print(multiply(5, 2))
# print(divide(9, 2))
#


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Anvarjon", "Sheraliev")

print(full_name)