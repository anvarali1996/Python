# name = input("enter your full name: ")
# phone_number = input("enter your phoneNumber: ")

# result = len(name)
# result = name.find("r")
# result = name.rfind("r")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isalpha()
# result = name.isdigit()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", "")



# ism = "Anvarjon"
# result = name.replace(name, ism)
# print(f"Do not lie!!! Your name is {ism}")



# print(phone_number)

# print(help(str))

# =========------TASK-----=========

# username = input("Enter a username:")
#
# if len(username) >= 12:
#     print("There 12 characters")
# #     BELOW IS also true. It works!!!
# # elif not username.find(" ") == -1:
# elif " " in username:
#     print("There is space")
# elif not username.isalpha():
#     print("There're some digits")
# else:
#     print(f"You have successfully regisreted!!! WELCOME {username}")


# ===============-------------- STRING INDEXING -------------==================

# indexing  = accessing elements of a sequence using [] (indexing operators)
#  [start: end: step]

credit_number = '1234-5678-9012-3456'

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2])

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# it shows on reverse form!!!
last_digits = credit_number[::-1]
print(last_digits)