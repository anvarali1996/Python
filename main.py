# Conditional expression = A one-line shortcut for the if-else statement (ternanry operator)
#             print or assign one of two based value based on a condition
#             X if condition else Y

num = 120
a = 5
b = 7
age = 16
temperature = 21
user_role = "guest"

# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b

# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)