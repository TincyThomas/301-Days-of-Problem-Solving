import re

pattern = "[.py.pyw]$"
print(bool(re.search(pattern, "/users/file.py")))
print(bool(re.search(pattern, "/users/file.pyw")))
print(bool(re.search(pattern, "/users/python/file.txt")))
