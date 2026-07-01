# total = 0

# for i in range(0, 6):
#     total += i

# print(total)

# Nested for loop
# for i in range(1, 4):
#     for j in range(1, 3):
#         for k in range(1, 5):
#             print(i, j, k)

# number = 5
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# Print the numbers from 1 to 20.
# for i in range(1, 21):
#     print(i)

# Print only the even numbers from 1 to 20.
# for i in range(2, 21, 2):
#     print(i)
    
# Print each letter in your name on a new line.
# name = input("Enter your name: ")
# for letter in name:
#     print(letter)

# Calculate the sum of numbers from 1 to 100.
# total = 0
# for i in range(1, 101):
#     total += i

# print(total)

# Print the 7-times multiplication table.
# number = 7
# for i in range(1, 21):
#     print(f"{number} x {i} = {number * i}")

# Loop through a list of your favorite foods and print: "I like <food>" for each one.
# foods = ["Egusi", "Fried Rice", "Akara", "Moi Moi"]
# for i in range(len(foods)):
#     print(f"I like {foods[i]}.")

# for counter in reversed(range(1, 11)):
#     print(counter)

# Nested loop

# row = 1
# while row <= 4:
#     col = 1
#     while col <= 5:
#         print("*", end=" ")
#         col += 1
        
#     print()
#     row += 1

# row = 1
# for row in range(1, 5):
#     for col in range(1, 6):
#         print("*", end=" ")
#     print()

# i = 1
# for i in range(1, 13):
#     for j in range(1, 21):
#         print(f"{i} x {j} = {i * j}")
#     print()

# i = 1
# while i <= 12:
#     j = 1
#     while j <= 20:
#         print(f"{i} x {j} = {i * j}")
#         j += 1
#     print()
#     i += 1

# Number Pattern
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(i, end=" ")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1

# i = 5
# while i >= 1:
#     j = 1
#     while j <= i:
#         print(i, end=" ")
#         j += 1
#     print()
#     i -= 1

# i = 5
# while i >= 1:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i -= 1

# servers = ["Server_A", "Server_B", "Server_C"]

# for server in servers:
#     status = "Disconnected"
#     attempts = 0
    
#     # Inner while loop handles dynamic, condition-driven retries
#     while status != "Connected" and attempts < 3:
#         attempts += 1
#         print(f"Pinging {server}... Attempt {attempts}")
#         # (Assuming some real check changes status here)
#         if attempts == 2:  # Simulating a successful connection
#             status = "Connected"
            
#     print(f"{server} status: {status}\n")

game_running = True
characters = ["Hero", "Mage", "Goblin"]

# Outer loop keeps the application alive indefinitely 
while game_running:
    print("--- New Game Turn ---")
    
    # Inner loop performs a predictable sequence of tasks
    for character in characters:
        print(f"Updating positions and graphics for: {character}")
        
    user_choice = input("Press Enter to continue or type 'quit': ")
    if user_choice.strip().lower() == 'quit':
        game_running = False  # Triggers exit of the outer while loop
