#### LISTS
# fruits = ["apple", "banana", "mango", "grape"]

# for fruit in fruits:
#     print(fruit)

# print(dir(fruits))  # Output: List of all attributes and methods of the list object
# print(help(fruits))  # Output: Help information about the list object
# print(len(fruits))  # Output: 4
# print("pineapple" in fruits)  # Output: False

# fruits[0] = "kiwi"  # Changing the first element
# fruits.append("orange")  # Adding a new element at the end
# fruits.remove("apple")  # Removing an element
# fruits.insert(1, "strawberry")  # Inserting an element at index 1
# fruits.sort()  # Sorting the list in ascending order
# fruits.reverse()  # Reversing the list
# fruits.pop()  # Removing the last element
# fruits.extend(["pineapple", "watermelon"])  # Adding multiple elements at the end
# print(fruits.count("banana"))  # Output: 1
# fruits.clear()  # Clearing all elements from the list

# print(fruits.index("banana"))  # Output: 1
# print(fruits)  # Output: []

#### SETS
# fruits = {"apple", "banana", "mango", "grape"}

# print(fruits)  # Output: {'banana', 'grape', 'mango', 'apple'}
# print(dir(fruits))  # Output: List of all attributes and methods of the set object
# print(help(fruits))  # Output: Help information about the set object
# print(len(fruits))  # Output: 4
# print("pineapple" in fruits)  # Output: False

# fruits.add("pineapple")  # Adding a new element
# fruits.remove("apple")  # Removing an element
# fruits.pop()  # Removing and returning an arbitrary element
# fruits.update(["kiwi", "watermelon"])  # Adding multiple elements
# fruits.discard("banana")  # Removing an element if it exists
# fruits.clear()  # Clearing all elements from the set

# print(fruits)  # Output: {'banana', 'grape', 'mango', 'kiwi', 'watermelon', 'pineapple'}

#### TUPLES
fruits = ("apple", "banana", "mango", "grape")

print(dir(fruits))  # Output: List of all attributes and methods of the tuple object
print(help(fruits))  # Output: Help information about the tuple object
print(len(fruits))  # Output: 4
print("pineapple" in fruits)  # Output: False
print(fruits.index("banana"))  # Output: 1
print(fruits.count("banana"))  # Output: 1

for fruit in fruits:
    print(fruit)

print(fruits)  # Output: ('apple', 'banana', 'mango', 'grape')
