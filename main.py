# Weight calculator

# weight = float(input("Enter your weight: "))
# unit = input("Kilogram or Pounds? (K or L): ")
#
# if unit == "K" or unit == "k":
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"Your weight is: {round(weight, 2)} {unit}")
#
# elif unit == "L" or unit == "l":
#     weight = weight / 2.205
#     unit = "Kgs"
#     print(f"Your weight is: {round(weight, 2)} {unit}")
#
# else:
#     print(f"{unit} was not valid")

# print(f"Your weight is: {round(weight, 2)} {unit}")

# ======= Tempurature Conversion ========

unit = input("Is the temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp}°F")
elif unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Fahrenheit is {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")