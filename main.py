# Typecasting = the process of converting a variable from type to
#  str(), int(), float(), bool()

# name = "Anvarjon"
# age = 28
# gpa = 3.8
# is_student = False
#
# name = bool(name)
# age = intf(gpa)
# # print(type(name))
# # print(str(age))
# # print(int(gpa))
# # print(type(is_student))
#
# print(age)

# ==============------ INPUT ------=================
# name = input("What is your name?")
# age = input("How old are you?")
#
# age = int(age)
# age = age + 1
# print(f"Hello {name}!!!")
# print("Happy BIRTHDAY")
# print(f"You are {age} years old!")

# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# area = length * width
#
# print(f"Are is {area}m²")

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?"))
total = price * quantity

print(f"you have bought {quantity} x {item}/s")
print(f"Your total is: $ {total}")