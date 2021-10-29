import re
txt1 = "Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts?"
txt2 = "Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts ?"

#pattern = "yourregularexpressionhere"
pattern = "\S\?"


print(bool(re.search(pattern, txt1)))
print(bool(re.search(pattern, txt2)))
