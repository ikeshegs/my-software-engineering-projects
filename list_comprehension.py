# 
numbers = [1, 2, 3, 4, 5, 6]

squares = [num ** 2 for num in numbers]  # This will create a new list with the squares of the numbers in the original list
print(squares)  # Output: [1, 4, 9, 16, 25, 36]

#
names = ["john", "alice", "ikechukwu", "doe"]

# cap_names = [name.upper() for name in names]  # This will create a new list with the names in uppercase
# print(cap_names)  # Output: ['JOHN', 'ALICE', 'IKECHUKWU', 'DOE']
cap_names = [name.capitalize() for name in names]
print(cap_names)  # Output: ['John', 'Alice', 'Ikechukwu', 'Doe']

#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

even_numbers = [num for num in numbers if num % 2 == 0]  # This will create a new list with only the even numbers from the original list
print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12]

#
words = ["cat", "elephant", "ezinne", "uche", "dan"]

short_words = [word for word in words if len(word) < 4]
print(short_words)  # Output: ['cat', 'dan']

#
scores = [34, 60, 85, 12, 80, 76, 30, 70, 92]

grades = ["pass" if score > 50 else "fail" for score in scores]

print(grades) # Output: ['fail', 'pass', 'pass', 'fail', 'pass', 'pass', 'fail', 'pass', 'pass']

# Flattening a Nested list
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = [num for row in matrix for num in row]

print(flat) # Output: [1, 2, 3, 4, 5, 6]

# Creating a list from a range()
numbers = [x for x in range(10)]

print(numbers) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extracting Data from Dictionaries
students = {
    "Alice": 85,
    "Bob": 90,
    "John": 70
}

scores = [score for score in students.values()]
names = [name for name in students.keys()]

print(scores) # Output: [85, 90, 70]
print(names) # Output: ['Alice', 'Bob', 'John']

pairs = [f"{name}: {score}" for name, score in students.items()]
print(pairs) # Output: ['Alice: 85', 'Bob: 90', 'John: 70']

# Combining Two lists
names = ["Alice", "Bob", "John"]
ages = [22, 38, 43]

combined = [f"{name} ({age})" for name, age in zip(names, ages)]
print(combined) # Output: ['Alice (22)', 'Bob (38)', 'John (43)']

# Nested List Comprehension
pairs = [(x, y) for x in [1,2,3] for y in ["A", "B"]]

print(pairs) # Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]

# 
sum_array = [x for x in range(1, 21)]
print(sum_array) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Create a list of cube
cubes = [x**3 for x in range(1, 11)]
print(cubes) # Output: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# Extract only vowels from a string.
letters = [x for x in "Ikechukwu" if x in "aeiou"]
print(letters) # Output: ['e', 'u']

# Remove empty strings from a list.
list_str = [" Ikechukwu", "Ezinne ", " Uche ", "  Dan"]
cleaned_str = [s.strip() for s in list_str]
print(cleaned_str) # Output: ['Ikechukwu', 'Ezinne', 'Uche', 'Dan']

#
