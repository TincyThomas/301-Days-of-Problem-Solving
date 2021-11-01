import re

#pattern = "yourregularexpressionhere"

pattern = "^/users/edabit/"

print(bool(re.search(pattern, "/users/edabit/python/regex.py")))
print(bool(re.search(pattern, "/users/edabitt/python/file.txt")))
print(bool(re.search(pattern, "/users/pyter/edabit/file.py")))
