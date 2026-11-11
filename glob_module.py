import glob

files = glob.glob("*.py")   # This finds all Python files in the directory.

# print(files)

files2 = glob.glob("*.txt")

# print(files2)

files3 = glob.glob("*")     # Match all the files in the folder

# print(files3)

### Match exactly one character
file = glob.glob("?ata.txt")

# print(file)     # print: ["data.txt"]

### [] (Character Sets)
file = glob.glob("[ef]*.py")

# print(file)     # Only files starting with "e" and "f" are matched

### Searching Inside Folders
files = glob.glob("OOP/*.py")

# print(files)

### Recursive Search
files = glob.glob("**/*.py", recursive=True)    # Search every Python file | "**" means search this directory and subdirectories

# print(files)

### Using iglob()
# for file in glob.iglob("*.py"):
#     print(file)
    
### Sorting Results
files = sorted(glob.glob("*.py"))

# print(files)

### Combining with File I/O
# for filename in glob.glob("*.txt"):
#     with open(filename, "r") as file:
#         print(f"Contents of {filename}:")
#         print(file.read())

### Example: Count Lines in Every Python File
# for filename in glob.glob("*.py"):
#     with open(filename) as file:
#         lines = len(file.readlines())

#     print(f"{filename}: {lines} lines")

### Example: Find Large Log Files
import os

for filename in glob.glob("*.log"):
    size = os.path.getsize(filename)

    if size > 1_000_000:
        print(filename)
        
### Using pathlib with glob
from pathlib import Path

folder = Path(".")  # The modern pathlib module provides similar functionality with an object-oriented interface.

# for file in folder.glob("*.py"):
#     print(file)

## Recursive search
for file in folder.rglob("*.py"):
    print(file)
