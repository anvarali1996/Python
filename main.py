# double = []
# for i in range(1, 11):
#     double.append(i * 2)
#
# print(double)

# numbers = [num for num in range(1, 11)]
# double = [x * 2 for x in range(1, 11)]
# triple = [x * 3 for x in range(1, 11)]
# square = [x * x for x in range(1, 11)]
#
# print(numbers)
# print(double)
# print(triple)
# print(square)

# fruits = ["apple", "orange", "strawberry", "pear"]
# fruits = [i.upper() for i in fruits]
# print(fruits)

numbers = [1, -2, 3, -4, 5, -6, 7, 9, 8, 87, 98]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num <= 0]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 != 0]

print(positive_num)
print(f"Negative numbers: {negative_num}")
print(even_num)
print(odd_num)
