import re
txt = "Hello!... Wait. How goes?..... GoodBye!.."
pattern = "\.{3,}"
print(re.findall(pattern, txt))
