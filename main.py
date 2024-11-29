# price1  = 3300.21233
# price2 = -223.22
# price3 =  22.122
#
# print(f"Price1 is ${price1:.2f}")
# print(f"Price2 is ${price2:.2f}")
# print(f"Price3 is ${price3:.3f}")



# ======----- WHILE LOOP -----========


# name = input("Enter your name: ")
#
# while name == "":
#     print("You didn't enter your name!!!")
#     name = input("Enter your name: ")
#
# print(f"Hello {name}!")

# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Age can't be negative!!!")
#     age = int(input("Enter your age: "))
#
# print(f"You're {age} years old!")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!!!")
    num = int(input("Enter a # between 1 - 10: "))


print(f"Your number is {num} !")
