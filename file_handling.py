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
with open("notes.txt", "r") as file:
    print(file.read())
    
## Checking if a File Exists
from pathlib import Path

path = Path("notes.txt")

# if path.exists():
#     print("File exists")
# else:
#     print("File does not exist")
    
## Handling File Errors
try:
    with open("missing.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
    
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

print(count)

### Search for a word
word = "Python"

with open("languages.txt") as file:
    for line in file:
        if word in line:
            print(line.strip())
