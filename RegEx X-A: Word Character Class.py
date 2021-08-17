import re
txt = "**^&$Regular#$%Expressions$%$$%^**"
pattern = re.findall(r'[\w\.-]+[\w\.-]+',txt)
a = ""
for i in pattern:
    a = a + " " + i
print(a)
