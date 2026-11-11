## Opening a file
file = open("log.txt", "r")

## Reading file
file = open("data.txt", "r")
content = file.read()

# print(content)

file.close()

## read(size)
file = open("data.txt", "r")
content = file.read(10)      # /Lorem ipsu/ Read the first six characters

# print(content)

file.close()

## readline() - This read one at a time
file = open("data.txt", "r")

# print(file.readline())
# print(file.readline())

file.close()

## readlines() - Reads all lines into a list
file = open("languages.txt", "r")

lines = file.readlines()

# print(lines)

file.close()

## Looping through a file
file = open("languages.txt", "r")

# for line in file:
#     print(line.strip())     # strip() removes the newline character.

file.close()

## Writing to a file
file = open("notes.txt", "w")

file.write("Python")

file.close()

## Writing multiple lines
file = open("notes.txt", "w")

file.write("SQL\n")
file.write("TypeScript\n")
file.write("Rust\n")

file.close()

## writelines() - Writes a list of strings.
languages = [
    "Python\n",
    "JavaScript\n",
    "PHP\n"
]

file = open("notes.txt", "w")

file.writelines(languages)

file.close()

## Appending to a file
file = open("notes.txt", "a")

file.write("\nC#")      # Adds a new line before appending C# on the next line

file.close()

## Creating a new file
# file = open("newfile.txt", "x")

# file.close()

# The Better Way: with
# with open("notes.txt", "r") as file:
#     print(file.read())
    
## Checking if a File Exists
from pathlib import Path

path = Path("notes.txt")

# if path.exists():
#     print("File exists")
# else:
#     print("File does not exist")
    
## Handling File Errors
# try:
#     with open("missing.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("The file does not exist.")
    
### Count Words in a File
with open("data.txt", "r") as file:
    text = file.read()

words = text.split()

# print(len(words))

### Copy a file
with open("notes.txt", "r") as source:
    content = source.read()

with open("newfile.txt", "w") as destination:
    destination.write(content)
    
### Count lines
count = 0

with open("notes.txt", "r") as file:
    for line in file:
        count += 1

# print(count)

### Search for a word
word = "Python"

# with open("languages.txt") as file:
#     for line in file:
#         if word in line:
#             print(line.strip())

### Exercise 1 - Create a file called students.txt and write the names of five students into it.
try:
    with open("students.txt", "x") as file:
        file.write("Jane Doe\n")
        file.write("John Doe\n")
        file.write("Emeka Ike\n")
        file.write("Emerald Eze\n")
        file.write("Uche Aja\n")
except FileExistsError:
    print("This file already exists.")
    
### Exercise 2 - Read students.txt and print each name on a separate line.
# with open("students.txt", "r") as file:
#     for line in file:
#         print(line.strip())
        
### Exercise 3 - Count how many lines are in students.txt.
count = 0

with open("students.txt") as file:
    for line in file:
        count += 1
        
# print(count)

### Exercise 4 - Append two more student names without deleting the existing ones.
with open("students.txt", "a") as file:
    file.write("Chioma Okoro\n")
    file.write("Ezinne Uwanta\n")
    
### Exercise 5 - Read the file again and print only the names that start with the letter "J".
word = "J"

with open("students.txt", "r") as file:
    for line in file:
        if word in line:
            print(line.strip())
            
### Exercise 6 - Copy the contents of students.txt into a new file called backup.txt.
with open("students.txt", "r") as source:
    content = source.read()
    
with open("backup.txt", "w") as destination:
    destination.write(content)
    
### Exercise 7 - Write a program that asks the user for a filename and prints its contents, displaying a friendly error message if the file doesn't exist.
file_name = input("What is the name of the file: ")

try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"This file, '{file_name}' does not exist.")
