
# name = input("What is your name? ")

# print(f"Hello, {name}")


# validate user input exercise
# 1. username must not contain spaces 
# 2. username is no more than 12 characters
# 3. username must not contain digits

# username = input("Enter a username: ")

# if " " in username:
#    print("Username cannot contain spaces.")
# elif len(username) > 12:
#    print("Username must be no more than 12 characters.")
# elif username.isdigit():
#    print("Username cannot contain digits.")
# else:
#    print(f"Username '{username}' is valid.")

# print(help(str))

# Format Specifiers
# price1 = 2300.35143345
# print(f"Price: ${price1:,.2f}")

# WHILE LOOP

# name = input("What is your name? ")
# while name == "":
#     print("Name cannot be empty. Please enter your name.")
#     name = input("What is your name? ")

# print(f"Hello, {name}!")

# num = int(input("Enter a number between 1 and 10: "))

# while num < 1 or num > 10:
#     print("Invalid input. Please enter a number between 1 and 10.")
#     num = int(input("Enter a number between 1 and 10: "))
    
# print(f"The number you entered is: {num}")

number = 10

while number > 0:
    print(number)
    number -= 1
    
print("Blast Off!")
