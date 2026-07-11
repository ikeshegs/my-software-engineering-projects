#
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

# 
command = "start"

match command:
    case "start":
        print("Starting.....")
    case "stop":
        print("Stopping.....")
    case "pause":
        print("Pausing.....")
    case "restarting":
        print("Restarting.....")
    case _:
        print("Unknown command")
        
# Matching Multiple Values
# You can use the | operator to match multiple possible values.
grade = "A"

match grade:
    case "A" | "B":
        print("Excellent")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case _:
        print("Fail")

# Matching Tuples
# Pattern matching can unpack tuples.

point = (3, 0)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"Point is on the x-axis at x={x}")
    case (0, y):
        print(f"Point is on the y-axis at y={y}")
    case (x, y):
        print(f"Point is at ({x}, {y})")
        
# Matching Lists
numbers = [1, 2]
# numbers = [1, 2, 3, 4, 5]

match numbers:
    case []:
        print("Empty list")
    case [x]:
        print(f"Single element list with value {x}")
    case [x, y]:
        print(f"Two element list with values {x} and {y}")
    case _:
        print("List has more than two elements")
        
# Using Guards (if)
# You can add conditions using if.
# The if after the pattern is called a guard. The case only matches if both the pattern and the guard are true.
age = 20

match age:
    case x if x < 18:
        print("Minor")
    case x if x >= 18:
        print("Adult")


# Menu Program
choice = input("Choose (1-3): ")

match choice:
    case "1":
        print("You selected Add")
    case "2":
        print("You selected Edit")
    case "3":
        print("Goodbye!")
    case _:
        print("Invalid choice")

