# from script2 import *
# def favorite_food(food):
#     print(f"Your favorite food is {food}")
#
# def main():
#     print("This is script1")
#     favorite_food('palov')
#     print("Good bye!!!")
#
# if __name__ == "__main__":
#     main()

# import random
# import string
#
# chars = "  " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()
#
# random.shuffle(key)
#
# print(f"chars: {chars}")
# print(f"key  : {key}")
#
# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    # cipher_text += key[index]
    plain_text += chars[index]

print(f"original message: {plain_text}")
print(f"encrypt message: {cipher_text}")

