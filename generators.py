# suppose you need a number from 1 - 10000
numbers = list(range(1, 10001))

# But using GENERATORS
numbers = (x for x in range(1, 1000001))

# Creating a generator function using "yield"
def count_to_three():
    yield 1
    yield 2
    yield 3
    
numbers = count_to_three()

# print(numbers)      # This print the genreator object Output: <generator object count_to_three at 0x0000023B1CC45C00>
# print(next(numbers))        # Output: 1
# print(next(numbers))        # Output: 2
# print(next(numbers))        # Output: 3
# print(next(numbers))        # Output: StopIteration

# It is prefer that you loop through the generator output
# for number in count_to_three():
#     print(number)

# Effect of using "yield"
def greetings():
    print("Hello")
    yield
    print("Welcome")

g = greetings()

# next(g)

# Generator Expressions
squares = (x * x for x in range(5))

# for square in squares:
#     print(square)

# Example: Reading a huge file
def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line

# for line in read_file("data.txt"):
    # print(line.strip())                 # This prints each line in the file.

# Infinite generators
def even_numbers():
    number = 0

    while True:
        yield number
        number += 2

evens = even_numbers()

# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))

# Chaining generators
def numbers():
    for i in range(20):
        yield i

def even_only(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

def square(nums):
    for num in nums:
        yield num * num

result = square(even_only(numbers()))

# for value in result:
#     print(value)

# Write a generator that yields the numbers from 1 to 20.
def numberss():
    for i in range(21):
        yield i
        
# for value in numberss():
#     print(value)


# Write a generator that yields only odd numbers from 1 to 50.
def odd_numbers():
    for num in range(50):
        if num % 2 == 1:
            yield num

# for value in odd_numbers():
#     print(value)

# Write a generator that yields the first 10 multiples of 7.
def seven_multiples():
    for num in range(1, 11):
        yield num *7

# for value in seven_multiples():
#     print(value)

# Create a generator expression that yields the cubes of numbers from 1 to 10.
def number_cubes():
    for num in range(1, 11):
        yield num ** 3
        
for value in number_cubes():
    print(value)

