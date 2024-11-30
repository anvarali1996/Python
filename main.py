# Python calculator

operator = input("Enter operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
    # print(num1 + num2)
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
    # print(num1 - num2)
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
    # print(num1 * num2)
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
    # print(num1 / num2)
else:
    print("Please write these 4 emblems")