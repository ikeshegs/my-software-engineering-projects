capitals = {
    "USA": "Washington D.C.",
    "China": "Beijing",
    "Russia": "Moscow", 
    "India": "New Delhi"
}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Chicago"})
# capitals.pop("China")
# capitals.popitem()  # This removes the last item in the dictionary
# capitals.clear()

# print(capitals)

# keys = capitals.keys()
# print(type(keys))
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(value)

# items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")
