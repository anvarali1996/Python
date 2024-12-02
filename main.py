#  ======--- DICTIONARY ---=====

capitals = {
    'USA': "Washington D.C.",
    "Uzbekistan": "Tashkent",
    "Latvia": "Riga",
    "UAE": "Abu Dhabi"
}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Uzbekistan"))

# if capitals.get("Lithuania"):
#     print("Frontend developer is here")
# else:
#     print("Backend developer is no here")

# capitals.update({"Germany": 'Berlin'})
# capitals.update({"USA": 'New York'})
# capitals.pop("USA")
# capitals.popitem()
# keys = capitals.keys()

# for keys in capitals.keys():
#     print(keys)

# below we can see the value (capital cities)
# values = capitals.values()
# print(values)

# for values in capitals.values():
#     print(values)

# ITEMS
for key, value in capitals.items():
    print(f"{key}: {value}")