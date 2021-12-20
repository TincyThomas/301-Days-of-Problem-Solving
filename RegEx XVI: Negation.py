import re
txt = "alice15@gmail.com"
txt1 = "901-333-"
pattern = "[^a-z|\d]"

print(re.findall(pattern, txt))
