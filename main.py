# import random
#
# low = 1
# high = 100
# options = ("rock", "scissors", "paper")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#
# # number = random.randint(low, high)
# # number = random.random()
# # options = random.choice(options)
# random.shuffle(cards)
#
# # print(f"{number:.2f}")
# print(cards)


# PYTHON number guessing game

import random

lowest_num = 1
highest_num = 10
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")