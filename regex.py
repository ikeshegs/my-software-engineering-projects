import re

### search() function - The search() function searches the string for a match, and returns a Match object if there is a match. If there is more than one match, only the first occurrence of the match will be returned
text = "I love Python"

match = re.search("Python", text)

# if match is not None:
#     print(match.group())    # 'group()' informs Python to print the matched text, without it, it prints an object  
# else:
#     print(match)
    
### Using match()
text = "Python is awesome"

# print(re.match("Python", text).group())
# print(re.match("awesome", text))    # This prints None since it isn't at the beginning

### findall() function - The findall() function returns a list containing all matches.
txt = "The rain in Spain"
x = re.findall("Spain", txt)
# print(x)

### split() function - The split() function returns a list where the string has been split at each match
txt = "The rain in Spain"
x = re.split(r"\s+", txt)
# print(x)

### using the maxsplit parameter in split()
txt = "The rain in Spain"
x = re.split(r"\s+", txt, maxsplit=1)
# print(x)

### sub() function - The sub() function replaces the matches with the text of your choice
txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
# print(x)

###  'count' parameter - You can control the number of replacements by specifying the count parameter.
txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt, count=2)
# print(x)

### Using the span() method in the Match Object
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
# print(x.span())     # (12, 17)
# print(x.string)     # The rain in Spain
# print(x.group())    # Spain

### fullmatch() - The entire string must match
x = re.fullmatch(r"\d+", "12345")
# print(x)

x = re.fullmatch(r"\d+", "abc123456")
# print(x)

### findall() - return every match
text = "cat dog cat bird"

matches = re.findall("cat", text)

# print(matches)

### finditer() - return match objects
text = "cat dog cat"

for match in re.finditer("cat", text):
    print(match.start(), match.end())


