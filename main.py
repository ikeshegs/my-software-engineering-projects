
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

# number = 10

# while number > 0:
#     print(number)
#     number -= 1
    
# print("Blast Off!")

# name = input("What is your name?: ")

# while name == "":
#     print("Name cannot be empty. Please enter your name.")
#     name = input("What is your name?: ")
    
# print(f"Hello, {name}!")

# passwd = input("Enter a password: ")

# while passwd != "passwd123":
#     print("Incorrect password. Please try again.")
#     passwd = input("Enter a password: ")
    
# print("Access granted!")

# secret_number = int(input("Guess the secret number (between 1 and 10): "))

# while secret_number != 7:
#     print("Incorrect guess. Please try again.")
#     secret_number = int(input("Guess the secret number (between 1 and 10): "))
    
# print("Congratulations!")

# ans = input("Do you want to add two numbers? (yes/no): ").lower()
# ans = "yes"

# while ans == "yes":
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
    
#     total = num1 + num2
#     print(f"The sum of {num1} and {num2} is: {total}")
    
#     ans = input("Do you want to add two numbers? (yes/no): ").lower()
    
# print("Goodbye")

# print("===MENU===")
# print("1. Say Hello")
# print("2. Tell a joke")
# print("3. Exit")

# option = input("Choose an option (1-3): ")

# while option != "3":
#     if option == "1":
#         print("Hello!")
#     elif option == "2":
#         print("Why don't scientists trust atoms?")
#         print("Because they make up everything!")
#     else:
#         print("Invalid option. Please choose again.")

#     option = input("Choose an option (1-3): ")

# print("Goodbye!")

while True:
    print("=== MENU ===")
    print("1. Say Hello")
    print("2. Tell a joke")
    print("3. Exit")
    
    option = input("Choose an option (1-3): ")
    
    if option == "1":
        print("Hello!")
    elif option == "2":
        print("Why don't scientists trust atoms?")
        print("Because they make up everything!")
    elif option == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose again.")


