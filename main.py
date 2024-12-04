# Iretable

# numbers = [1, 2, 4, 5, 6]
# for number in reversed(numbers):
#     print(number, end=" ")

# name = "Anvarjon Sheraliev"
#
# for letter in name:
#     print(letter.upper(), end="")

# my_test = {"A": 1, 'B': 2, "C": 3}
#
# for key, value in my_test.items():
#     # print(f"{key}: {value}")
#     print(key, value)


# //////=====----- MEMBERSHIP OPERATORS -----======//////

# word = "APPLE"
#
# letter = input("Guess a letter in the secret word: ")
#
# # if letter in word:
# #     print(f"There is a {letter}")
# # else:
# #     print(f"{letter} was not found")
#
# if letter not in word:
#     # print(f"There is a {letter}")
#     print(f"{letter} was NOT found")
#
# else:
#     print(f"{letter} was found")

# students = {"Ali", "Bob", "Someone"}
#
# student = input("enter a student name: ")
#
# if student in students:
#     print(f"{student} is student")
# else:
#     print(f"{student} was not found!!!")

# grades = {"Ali": 1, "Bob": "5-score", "Someone": "8 score"}
# student = input("Enter the name of student: ")
#
# # if student in grades:
# #     print(f"{student}'s grade is {grades[student]}")
# # else:
# #     print(f"{student} was not found")
#
# for key, value in grades.items():
#     print(student)
#     print(f"{key}: {value}")


email = "info@anvarjon.eu"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")