# DEFAULT ARGUMENTS
# def net_price(list_price, discount = 0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)
#
# # print(net_price(500))
# # print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))


# import time
# def count(start, end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE")
#
# count(1, 10)

# KEY ARGUMENTS

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")
#
# hello("Hello", title="Mr.", last="John", first="James")

# for x in range(1, 11):
#     print(x, end=" ")

# print("1","2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=998, area=93, first=299, last=4343)
print(phone_num)